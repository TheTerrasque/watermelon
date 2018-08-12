from django.db import models
from django.utils import timezone



class Platform(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class SongStatus(models.Model):
    name = models.CharField(max_length=200)
    visible = models.BooleanField()

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey('auth.User', related_name='songs', on_delete=models.SET_NULL, blank=True, null=True)
    artist = models.ForeignKey('artists.Artist', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    added = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(SongStatus, on_delete = models.CASCADE)

    last_queued = models.DateTimeField(blank=True, null=True)
    last_played = models.DateTimeField(blank=True, null=True)
    replay_gain = models.FloatField(default=0)
    length = models.FloatField(blank=True, null=True)
    samplerate = models.IntegerField(blank=True, null=True)
    songtype = models.CharField(blank=True, max_length=20)
        # The uploaded file.
    file = models.FileField(upload_to='songsdata/%Y/%m/%d/')
    
    def get_streamer_data(self):
        return {
            'path': self.file.path, #pylint: disable=E1101
            'artist': self.artist.name,
            'title': self.name,
            'gain': str(self.replay_gain),
        }

    def can_be_queued(self):
        return not self.last_queued or self.last_queued < timezone.now() - timezone.timedelta(hours=12)

    def editable_by(self, user):
        return self.uploaded_by == user and self.added > timezone.now() - timezone.timedelta(minutes=10)

    def __str__(self):
        return self.name

    @classmethod
    def get_next_queued(cls):
        if cls.objects.count(): #pylint: disable=E1101
            song = cls.objects.order_by('?').first() #pylint: disable=E1101
            song.last_played = timezone.now()
            song.save()
            return song.get_streamer_data()
        return None