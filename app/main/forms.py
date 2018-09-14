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
    title = TextAreaField('Title.',validators = [Required()])
    subtitle = TextAreaField('Subtitle.',validators = [Required()])
    content = TextAreaField('Content',validators = [Required()])
    submit = SubmitField('Submit')

