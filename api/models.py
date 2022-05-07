from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
	users = models.ForeignKey(User,on_delete=models.CASCADE)
	title = models.CharField(max_length=255)
	description= models.TextField()
	deadline = models.DateTimeField()
	isCompleted= models.BooleanField(default=False)
