from django import forms


class MusicForm(forms.Form):
    title = forms.CharField(max_length=255)
    link = forms.CharField(max_length=255)
    authorName = forms.CharField(widget=forms.Textarea)
    authorEmail = forms.EmailField()