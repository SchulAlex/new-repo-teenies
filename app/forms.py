from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class StoryForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=1, max=100)])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit')


class PollForm(FlaskForm):
    question = StringField('Question', validators=[DataRequired()])
    options = StringField('Options (comma separated)', validators=[DataRequired()])
    submit = SubmitField('Create Poll')


class FeedbackForm(FlaskForm):
    name = StringField('Your Name', validators=[Length(max=50)])
    feedback = TextAreaField('Feedback', validators=[DataRequired()])
    submit = SubmitField('Send Feedback')
