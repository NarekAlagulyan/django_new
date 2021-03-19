from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


# where to upload user uploaded images
POST_IMAGES_STORAGE = 'post_images'

PROFILE_IMAGES_STORAGE = 'profile_images'


class Post(models.Model):

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
    title = models.CharField(max_length=100, verbose_name='Post title')
    content = models.TextField(verbose_name='Post content')

    image = models.ImageField(
        upload_to=POST_IMAGES_STORAGE,
        null=True,
        blank=True,

    )

    pub_date = models.DateTimeField(auto_now_add=True)
    up_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} | POST'

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=User)
    image = models.ImageField(
        upload_to=PROFILE_IMAGES_STORAGE,
        default=r'media/profile_images/def.png',
        verbose_name='Profile image'
    )
    phone = models.CharField(max_length=100, blank=True, null=True, verbose_name='Phone number')
    address = models.CharField(max_length=100, blank=True, null=True, verbose_name='Address')

    def __str__(self):
        return f'{self.user.username} | PROFILE'

    def get_absolute_url(self):
        return reverse('user-profile', kwargs={'pk': self.pk})

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url



