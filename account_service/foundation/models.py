from django.db import models
class UserMemoryDB(models.Model):
    username = models.CharField(max_length = 50)
    fname = models.CharField(max_length = 50)
    lname = models.CharField(max_length = 50)
    email = models.EmailField()
    password = models.TextField()
