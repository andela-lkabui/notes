from django.contrib.auth.models import User

from rest_framework import viewsets, status
from rest_framework.response import Response

from api import serializers, models


class UserViewSet(viewsets.ModelViewSet):
    """
    Viewset to enable CRUD operations on the User resource.
    """
    queryset = models.NotesUser.objects.all()
    serializer_class = serializers.UserSerializer

    def create(self, request, pk=None):
        """
        customize user post operation
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = models.NotesUser(username=serializer.validated_data['username'])
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response(
                {
                    'username': serializer.validated_data['username']
                }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteViewSet(viewsets.ModelViewSet):
    """
    Viewset to enable CRUD operations on the User resource.
    """
    queryset = models.Notes.objects.all()
    serializer_class = serializers.NoteSerializer
