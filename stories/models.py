# stories/models.py
from django.db import models
from users.models import CustomUser

class Story(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='authored_stories')
    co_authors = models.ManyToManyField(CustomUser, related_name='coauthored_stories', blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    votes = models.IntegerField(default=0)

class MultimediaElement(models.Model):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='multimedia')
    image = models.ImageField(upload_to='story_images/', null=True, blank=True)
    audio = models.FileField(upload_to='story_audio/', null=True, blank=True)
    video = models.FileField(upload_to='story_videos/', null=True, blank=True)
