from wtforms import Form, StringField, TextAreaField, validators
class CreateUserForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=150),validators.DataRequired()])
    email = StringField('Email',[validators.Length(min=1,max=60),validators.Email(),validators.DataRequired()])
    message = TextAreaField('Message',[validators.Length(min=1,max=600),validators.DataRequired()])