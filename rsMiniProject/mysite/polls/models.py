import datetime
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils import timezone

class Question(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, default=int(1))
    question_text=models.CharField(max_length=200)
    description=models.TextField(default='No description')
    pub_date = models.DateTimeField('date published',default=timezone.now)
    voters= ArrayField(models.IntegerField(blank=True))

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now=timezone.now()
        return now-datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text=models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    allowed=models.BooleanField(default=True)

    def __str__(self):
        return self.choice_text

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE, default=int(1))
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    comment_text=models.TextField()
    pub_date=models.DateTimeField('date published',default=timezone.now)

    def __str__(self):
        return self.comment_text[:10]
