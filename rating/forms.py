from django import forms
from .models import Project, Profile, Rating

RATING= [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

class UploadForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('design', 'usability', 'creativity', 'content', 'overall', 'posted', 'user' )
