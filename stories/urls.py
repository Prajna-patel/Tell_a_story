# stories/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_story, name='create_story'),
    # Add more paths for story details, voting, etc.
]
