from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):

    def url(self, filename):

        ruta = "MultimediaData/User/{}/{}"
        return ruta.format(self.user.username, self.user.username)

    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=url)
    telefono = models.CharField(max_length=30)

    def __unicode__(self):
        return self.user.username

