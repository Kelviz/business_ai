from django.db import models
from django.contrib.auth.models import User
from account.models import UserAccount
from ckeditor.fields import RichTextField


class BusinessAI(models.Model):
    industry = models.CharField(max_length=500)
    audience = models.CharField(max_length=500)
    budget = models.CharField(max_length=20)
    idea = RichTextField(blank=True, null=True)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=500)

    def __str__(self):
        return f'Business idea about {self.industry} targeting {self.audience} with the  budget of {self.budget}'


class About(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    image = models.ImageField(upload_to='images')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ScrollCard(models.Model):
    icon = models.ImageField(upload_to='icons')
    industry = models.CharField(max_length=400)
    idea = models.TextField()

    def __str__(self):
        return self.industry
