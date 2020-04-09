from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(label='Your password', max_length=100 , widget=forms.PasswordInput)

class SignUpForm(forms.Form):
    first_name = forms.CharField(label='Your first name', max_length=100)
    last_name = forms.CharField(label='Your last name', max_length=100)
    phone_number = forms.IntegerField(label='Your phone number')
    email = forms.CharField(label='Your email', max_length=120)
    username = forms.CharField(label='Your username', max_length=100)
    password = forms.CharField(label='Your password', max_length=100,widget=forms.PasswordInput)