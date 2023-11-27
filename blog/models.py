from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # date_posted = models.DateTimeField(auto_now=True)
    # date_posted = models.DateTimeField(auto_now_add=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, db_constraint=False)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})