from django.db import models
from users.models import CustomUser

class Achievement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class UserAchievement(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    achieved_on = models.DateTimeField(auto_now_add=True)
