from django.contrib.auth.models import User

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from api import serializers, models, custom_permissions


class UserViewSet(viewsets.ModelViewSet):
    """
    Viewset to enable CRUD operations on the User resource.
    """
    queryset = models.NotesUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (
        # permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsUserOwner,
    )

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

    def update(self, request, pk=None):
        user = models.NotesUser.objects.get(pk=request.user.id)
        user.set_password(request.data['password'])
        user.save()
        return Response(
                {
                    'details': "User password updated"
                }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteViewSet(viewsets.ModelViewSet):
    """
    Viewset to enable CRUD operations on the User resource.
    """

    permission_classes = (
        custom_permissions.IsNoteOwner,
    )
    queryset = models.Notes.objects.all()
    serializer_class = serializers.NoteSerializer

    def create(self, request, pk=None):
        """
        customize note post operation
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            note = models.Notes(**serializer.validated_data)
            note.owner = request.user
            note.save()
            resp = serializer.validated_data.copy()
            resp['id'] = note.id
            return Response(resp, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        """
        returns all the notes belonging to the user who is currently logged in.
        """
        queryset = models.Notes.objects.filter(owner=request.user)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


@api_view()
@permission_classes((permissions.IsAuthenticated,))
def whoami(request):
    return Response(
        {
            "username": request.user.username,
            "id": request.user.id
        }, status=status.HTTP_200_OK)
