from django import forms

class sign_up_form(forms.Form):
    name_form = forms.CharField(
        label='نام کاربری',
        max_length=50,
    )
    email_form = forms.EmailField(
        label='ایمیل',
    )
    password_form = forms.CharField(min_length=6,max_length=30,label='رمز عبور')

class log_in_form(forms.Form):
    Logname = forms.CharField(
        label='نام کاربری',
        max_length=50,
    )
    Logpassword = forms.CharField(min_length=6, max_length=30, label='رمز عبور')