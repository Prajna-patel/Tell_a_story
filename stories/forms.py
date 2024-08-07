# stories/forms.py
from django import forms
from .models import Story, MultimediaElement

class StoryForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ['title', 'content']

class MultimediaForm(forms.ModelForm):
    class Meta:
        model = MultimediaElement  # Corrected model name
        fields = ['image', 'audio', 'video']  # Adjust fields according to your model
