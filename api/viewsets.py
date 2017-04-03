from django.contrib.auth.models import User

from rest_framework import viewsets

from api import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    Viewset to enable CRUD operations on the User resource.
    """
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer