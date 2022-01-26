from django import forms


class UserForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Почта'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Имя"}))
    second_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Фамилия"}))
