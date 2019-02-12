from django.db import models
from django.contrib.auth.models import User

# this "Player" model class links one-to-one with a user (for adding fields to users)
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    def __str__(self):
        return '%s: %s %s' % ( self.user.username, self.user.first_name, self.user.last_name )
