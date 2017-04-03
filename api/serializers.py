from django.contrib.auth.models import User

from rest_framework import serializers

from api import models


class UserSerializer(serializers.ModelSerializer):
    """
    Serializes the User object
    """
    class Meta:
        model = User
        fields = ('username', )
        write_only_fields = ('password',)


class NoteSerializer(serializers.ModelSerializer):
    """
    Serializes the User object
    """
    class Meta:
        model = models.Notes
        fields = ('title', 'note', 'owner')