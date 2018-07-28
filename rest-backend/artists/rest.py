from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from rest_framework import permissions

from . import models
from songs.permissions import EditableByCheck

from mqtt_connection import mqtt_wrap

class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Artist
        fields = ("id", "name", "real_name", "country_code", "bio")

mqtt_wrap.S[models.Artist] = ArtistSerializer

class ArtistViewSet(viewsets.ModelViewSet):
    queryset = models.Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      EditableByCheck,)

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)
