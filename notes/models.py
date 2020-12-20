from django.db import models

from django.contrib.auth.models import User

# A note can have several tags that describe the category of the note
class Tag(models.Model):
    tag = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return self.tag

class Entry(models.Model):
    subject = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('note date')
    tag = models.ManyToManyField(Tag)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.subject
