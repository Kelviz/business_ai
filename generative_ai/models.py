from django.db import models
from django.contrib.auth.models import User

class BusinessAI(models.Model):
    industry = models.CharField(max_length=500)
    audience = models.CharField(max_length=500)
    budget = models.CharField(max_length=20)
    idea = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=500)

    def __str__(self):
        return f'Business idea about {self.industry} targeting {self.audience} with the  budget of {self.budget}'
