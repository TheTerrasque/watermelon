from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    real_name = models.CharField(max_length=200)

    country_code = models.CharField(max_length=2, blank=True)

    bio = models.TextField(blank=True)
    added = models.DateTimeField(auto_now_add=True)
    added_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.name + " (" + self.real_name + ") [" + self.country_code + "]"
