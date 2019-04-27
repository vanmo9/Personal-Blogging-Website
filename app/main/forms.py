from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    body = StringField('Your name',validators=[Required()])
    category = StringField('Give Your Blog' ,validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Comment Blog',validators = [Required()])
    submit = SubmitField('Submit')  