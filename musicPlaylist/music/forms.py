from django import forms


class MusicForm(forms.Form):
    title = forms.CharField(label="Title", max_length=255)
    link = forms.CharField(label="Link", max_length=255)
    authorName = forms.CharField(label="Author Name", widget=forms.Textarea)
    authorEmail = forms.EmailField()