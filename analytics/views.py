from django.shortcuts import render
from stories.models import Story

def analytics_dashboard(request):
    user_stories = Story.objects.filter(author=request.user)
    analytics_data = {
        'total_stories': user_stories.count(),
        'total_views': sum(getattr(story, 'views', 0) for story in user_stories),
        'total_votes': sum(story.votes for story in user_stories),
    }
    return render(request, 'analytics/analytics_dashboard.html', {'analytics_data': analytics_data})
