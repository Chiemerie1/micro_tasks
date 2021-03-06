from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django_countries.fields import CountryField

# Create your models here.




# class User(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.username


class Profile(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=13)
    token = models.PositiveIntegerField(default=0, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = CountryField(default=0, blank_label="(select country)")

    def __str__(self):
        return self.user.username


class Performer(models.Model):
    performed = models.BooleanField(default=False, verbose_name="Performer")
    # initiator = models.BooleanField(Initaitor, default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.performed


class Event(models.Model):
    FACEBOOK = 0
    YOUTUBE = 1
    TWITTER = 2
    INSTAGRAM = 3
    TIKTOK = 4
    SNAPCHAT = 5
    
    SOCIAL_MEDIA = (
                    (FACEBOOK, "Facebook"),
                    (YOUTUBE, "YouTube"),
                    (TWITTER, "Twitter"),
                    (INSTAGRAM, "Instagram"),
                    (TIKTOK, "TikTok"),
                    (SNAPCHAT, "Snapchat"),
                )

    num_of_followers_req = models.IntegerField(default=0)
    event_name = models.CharField(max_length=50)
    event = models.PositiveSmallIntegerField(choices=SOCIAL_MEDIA, default=INSTAGRAM,
                 max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event_name