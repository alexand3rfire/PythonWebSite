from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Test(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Question(models.Model):
    id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=255)
    correct = models.CharField(max_length=3)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

class Answer(models.Model):
    id = models.IntegerField(primary_key=True)
    letter = models.CharField(max_length=3)
    answer = models.CharField(max_length=255)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer

