from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

def profilePath(instance, filename):
    return "profile_pics/user_{0}/{1}". format(instance.id,filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, blank=True, null=True)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to=profilePath)


    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self, *args, **kwargs):
        """This will overide the save method to resize the image"""
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

