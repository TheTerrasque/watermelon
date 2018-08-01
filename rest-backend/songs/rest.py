from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from rest_framework import permissions

from songs import models
from .permissions import EditableByCheck
from rest_framework.decorators import action
from rest_framework.response import Response

from mqtt_connection import mqtt_wrap

class RelativeUrlModelSerializer():
    def get_serializer_context(self):
        """
        Extra context provided to the serializer class.
        """
        return {
            'request': None,
            'format': self.format_kwarg,
            'view': self
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'is_staff')

class SongSerializer(serializers.HyperlinkedModelSerializer):
    uploaded_by = serializers.ReadOnlyField(source='uploaded_by.username')
    #status = serializers.ReadOnlyField()
    #last_queued = serializers.ReadOnlyField()
    #file = serializers.FileField(use_url = False)
    
    class Meta:
        model = models.Song
        fields = ("id", "name", "platform", "artist", "uploaded_by", 
            "description", "added", "status", "file", "last_queued",
            "can_be_queued")


class PlatformSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.Platform
        fields = ("id", "name", "description")

class SongStatusSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = models.SongStatus
        fields = ("id", "name", "visible")

mqtt_wrap.S[models.Song] = SongSerializer
mqtt_wrap.S[models.SongStatus] = SongStatusSerializer
mqtt_wrap.S[models.Platform] = PlatformSerializer

class SongStatusViewSet(RelativeUrlModelSerializer,viewsets.ReadOnlyModelViewSet):
    queryset = models.SongStatus.objects.all()
    serializer_class = SongStatusSerializer

class UserViewSet(RelativeUrlModelSerializer, viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SongViewSet(RelativeUrlModelSerializer, viewsets.ModelViewSet):
    queryset = models.Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      EditableByCheck,)

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

    @action(detail=True)
    def can_queue(self, request, *args, **kwargs):
        """
        Return if the song can be queued
        """
        song = self.get_object()
        return Response({"queueable": song.can_be_queued()})

class PlatformViewSet(RelativeUrlModelSerializer, viewsets.ReadOnlyModelViewSet):
    queryset = models.Platform.objects.all()
    serializer_class = PlatformSerializer
