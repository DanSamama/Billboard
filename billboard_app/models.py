import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Message(models.Model):
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    def posted_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


