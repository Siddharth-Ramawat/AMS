from django.contrib.postgres.fields import ArrayField, IntegerRangeField
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    """
    User objects have the following fields
    username
    first_name
    last_name
    email
    password
    event_id
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    dept = models.CharField(max_length=120, blank=True, null=True)
    registration_number = models.CharField(max_length=12, blank=True, null=True)
    event_ids = models.TextField(null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    # Resizing the image to a smaller size
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

