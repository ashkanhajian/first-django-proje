from django import forms
from .models import *


class CreatPost(forms.ModelForm):
    image1 = forms.ImageField(label='image 1', required=False)

    class Meta:
        model = Post
        fields = ['title', 'description', 'reading_time', 'category']


class TicketForm(forms.Form):
    Subject_Choice = (
        ("پیشنهاد", "پیشنهاد"),
        ("انتقاد", "انتقاد"),
        ("گزارش مشکل", "گزارش مشکل")
    )
    message = forms.CharField(widget=forms.Textarea, required=True)
    name = forms.CharField(max_length=250, required=True)
    email = forms.EmailField()
    phone = forms.CharField(max_length=11, required=True)
    subject = forms.ChoiceField(choices=Subject_Choice)

    def clean(self):
        phone = self.cleaned_data['phone']
        if phone:
            if not phone.isnumeric():
                raise forms.ValidationError("enter just number")
            else:
                return phone


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        widgets = {
            'body': forms.TextInput(attrs={
                'placeholder': 'body',
                'class': 'Commentbody'
            })
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if name:
            if len(name) < 3:
                raise forms.ValidationError('your name is short')
            else:
                return name


class SearchForm(forms.Form):
    query = forms.CharField()


# class LoginForm(forms.Form):
#     username = forms.CharField(max_length=250, required=True)
#     password = forms.CharField(max_length=250, required=True, widget=forms.PasswordInput)
class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput, label='password')
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput, label='repeat password')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('passwords do not match')
        return cd['password2']


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'last_name']


class EditAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['date', 'bio', 'img', 'job']
