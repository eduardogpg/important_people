from wtforms import Form
from wtforms import TextField
from wtforms import PasswordField
from wtforms.fields.html5 import EmailField
from wtforms import HiddenField

from wtforms import validators

def length_honeypot(form, field):
	if len(field.data) > 0:
		raise validators.ValidationError('Lo siento bot no vas a pasar')

class LoginForm(Form):
	username = TextField('Username',[validators.Required(message = 'El username es requerido')])
	password = PasswordField('Password', [validators.Required(message='El password es requerido')])
	honeypot = HiddenField("",[ length_honeypot ])

class CreateForm(Form):
	username = TextField('Username', [
							validators.Required(message = 'El username es requerido.'),
							validators.length(min=4, max=25, message='Ingrese un username valido.') ])
	email = EmailField('Correo electronico',[
							validators.Required(message = 'El email es requerido.'),
							validators.Email(message='Ingre un email valido.'),
							validators.length(min=4, max=25, message='Ingrese un email valido.') ])
	password = PasswordField('Password', [validators.Required(message='El password es requerido')])
	honeypot = HiddenField("",[ length_honeypot ])
