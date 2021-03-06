from rest_framework import viewsets, filters
from rest_framework.authentication import TokenAuthentication

from . import permissions
from .serializers import UserProfileSerializer
from .models import UserProfile


class UserProfileViewSet(viewsets.ModelViewSet):

    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)