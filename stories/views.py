# stories/views.py
from django.shortcuts import render, redirect
from .forms import StoryForm, MultimediaForm
from .models import Story, MultimediaElement

def create_story(request):
    if request.method == 'POST':
        story_form = StoryForm(request.POST)
        multimedia_form = MultimediaForm(request.POST, request.FILES)
        if story_form.is_valid() and multimedia_form.is_valid():
            story = story_form.save(commit=False)
            story.author = request.user
            story.save()
            multimedia = multimedia_form.save(commit=False)
            multimedia.story = story
            multimedia.save()
            return redirect('story_list')
    else:
        story_form = StoryForm()
        multimedia_form = MultimediaForm()
    return render(request, 'stories/create_story.html', {'story_form': story_form, 'multimedia_form': multimedia_form})
