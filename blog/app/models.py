from django.db import models
from django.contrib.auth.models import User

STATUS = ((0,"Draft"), (1,"Published"))

class Post(models):
    title = models.CharField()

