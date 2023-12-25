from django import forms

class PostBlogForm(forms.Form):
    date = forms.DateField()
    writer = forms.CharField()
    title = forms.CharField()
    blog = forms.CharField()
