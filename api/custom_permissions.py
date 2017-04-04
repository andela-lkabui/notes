from rest_framework import permissions


class IsNoteOwner(permissions.BasePermission):
    """
    perimssions resrtict unsafe methods on notes to the owner
    """

    def has_object_permission(self, request, view, obj):
        """
        determmine access to unsafe operations based on currently logged in
        user
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.owner == request.user


class IsUserOwner(permissions.BasePermission):
    """
    restricts unsage methods to the user
    """

    def has_object_permission(self, request, view, obj):
        """
        determine rights to delete a user based on currently logged in user
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.id == request.user.id
