from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model
    )
User = get_user_model()

class registerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'first_name',
            'last_name'
        ]

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        if username and email:
            usr_exist = User.objects.filter(username__iexact=username).exists()
            em_exist = User.objects.filter(email__iexact=email).exists()
            if usr_exist:
                raise forms.ValidationError(
                    "A user with that  username already exists."
                )
            if em_exist:
                raise forms.ValidationError("This email already exists.")
        return super(registerForm, self).clean(*args, **kwargs)


class loginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            usr_qs = User.objects.filter(username__iexact=username)
            if usr_qs:
                username = usr_qs[0].username
                user = authenticate(username=username, password=password)
                if not user:
                    raise forms.ValidationError(
                        "The entered password seems incorrect please check "
                    )
            else:
                email_qs = User.objects.all().filter(email__iexact=username)
                if email_qs:
                    username = email_qs[0].username
                    # print(username)
                    user = authenticate(username=username, password=password)
                    if not user:
                        raise forms.ValidationError(
                            "The entered password seems incorrect please check "
                        )
                else:
                    raise forms.ValidationError("This user does not exist")
            if not user.is_active:
                    raise forms.ValidationError(
                        "This user is no longer active."
                    )
        else:
            raise forms.ValidationError(
                "Oops! something went wrong please try again"
            )
        if username and not password:
            raise forms.ValidationError(
                "Oops! We did not receive any password"
            )
            return username
        return super(loginForm, self).clean(*args, **kwargs)


class dashForm(forms.Form):
    country = forms.CharField()
    phone_num = forms.CharField()
