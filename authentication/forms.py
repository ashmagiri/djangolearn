from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=63)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )
