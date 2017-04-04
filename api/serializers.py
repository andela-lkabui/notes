from django.contrib.auth.models import User

from rest_framework import serializers

from api import models


class UserSerializer(serializers.ModelSerializer):
    """
    Serializes the User object
    """
    notes_set = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name='notes-detail')

    class Meta:
        model = models.NotesUser
        fields = ('username', 'password', 'notes_set')
        extra_kwargs = {
            'password': {'write_only': True}
        }


class NoteSerializer(serializers.ModelSerializer):
    """
    Serializes the User object
    """
    class Meta:
        model = models.Notes
        fields = ('title', 'note', 'owner')
        read_only_fields = ('owner',)
