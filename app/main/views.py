from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import *
from ..models import *
from flask_login import login_required, current_user
from .. import db,photos
import markdown2


@main.route('/')
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()

    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)

@main.route('/add')
def add():
    form=AddPost()
    return render_template('add.html', form=form)

@main.route('/addpost', methods=['GET', 'POST'])
def addpost():
    form = AddPost()
    if form.validate_on_submit():
        title = form.title.data
        subtitle = form.subtitle.data
        content = form.content.data

        post = Post(title=title, subtitle=subtitle, content=content, user_id=current_user.id, date_posted=datetime.now())


        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.addpost',form=form ))


    return redirect(url_for('main.index',form=form))



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required

def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))