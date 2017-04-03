from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Serializes the User object
    """
    class Meta:
        model = User
        fields = ('username', )
        write_only_fields = ('password',)