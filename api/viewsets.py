from django.contrib.auth.models import User

from rest_framework import viewsets

from api import serializers, models


class UserViewSet(viewsets.ModelViewSet):
    """
    Viewset to enable CRUD operations on the User resource.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    Viewset to enable CRUD operations on the User resource.
    """
    queryset = models.Notes.objects.all()
    serializer_class = serializers.NoteSerializer