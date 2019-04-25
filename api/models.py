from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class NotesUser(User):
    """
    customize user class
    """
    def get_notes(self):
        return self.notes_set.all()


class Notes(models.Model):
    """
    ORM for notes
    """
    title = models.CharField(max_length=100, blank=False)
    note = models.CharField(max_length=140, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)