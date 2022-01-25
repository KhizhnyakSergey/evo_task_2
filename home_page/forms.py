from django import forms


class UserForm(forms.Form):
    email = forms.EmailField()
    first_name = forms.CharField()
    second_name = forms.CharField()
