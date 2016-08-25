from django import forms

class NewAccountForm(forms.Form):
	username = forms.CharField(label='Username', max_length=30)
	password = forms.CharField(widget=forms.PasswordInput(), label='Password', max_length=20)
	email = forms.EmailField(label='Email')
	first_name = forms.CharField(label='First Name', max_length=20)
	last_name = forms.CharField(label='Last Name', max_length=20)