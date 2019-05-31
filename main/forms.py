from django import forms
from .models import Song

class DownloadForm(forms.ModelForm):
    class Meta:
        model = Song
        exclude = ['link', 'email']
    url = forms.RegexField(regex=r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$')
    email = forms.EmailField(label="Email Address")
    # message = forms.CharField(
    #     label="Message", widget=forms.Textarea(attrs={'rows': 5}))

    def __unicode__(self):
        return "Request " + '#' + str(self.id)



