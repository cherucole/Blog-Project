from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')



class CommentForm(FlaskForm):
    comment = TextAreaField('Leave your comment...',validators = [Required()])
    submit = SubmitField('Submit')


class AddPost(FlaskForm):
    title = TextAreaField('Title.')
    subtitle = TextAreaField('Subtitle.')
    content = TextAreaField('Content')
    submit = SubmitField('Submit')


class SubscriberForm(FlaskForm):

    email = StringField('Your Email Address...')
    name = StringField('Enter your name')
    submit = SubmitField('Subscribe')

