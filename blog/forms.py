from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class LoginForm(forms.Form):
    username = forms.CharField(label="Username/Email")
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    username.widget.attrs.update({'class': 'form-control'})


class SignUpForm(forms.Form):
    fname = forms.CharField(label="First Name", max_length=30)
    lname = forms.CharField(label="Last Name", max_length=30)
    email = forms.EmailField(max_length=250)
    YEARS = [x for x in range(1920, 2019)]
    dob = forms.DateField(label='Date of Birth', initial="1990-01-01",
                          widget=forms.SelectDateWidget(years=YEARS))

    fname.widget.attrs.update({'class': 'form-control'})
    lname.widget.attrs.update({'class': 'form-control'})
    email.widget.attrs.update({'class': 'form-control'})
    dob.widget.attrs.update({'class': 'form-col'})
