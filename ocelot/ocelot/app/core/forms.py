from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='', max_length=30, error_messages={}, widget=forms.TextInput(attrs={'class':'span2',}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'span2',}))
