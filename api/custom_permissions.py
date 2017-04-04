from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    perimssions resrtict unsafe methods to the owner
    """

    def has_object_permission(self, request, view, object):
        """
        determmine access rights based on currently logged in user
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return object.owner == request.user
