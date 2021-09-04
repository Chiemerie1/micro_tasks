from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

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

    def __str__(self):
        return self.username



class Initaitor(models.Model):
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    initiated = models.PositiveSmallIntegerField(verbose_name="Initiated", choices=SOCIAL_MEDIA, default=INSTAGRAM)

    def __str__(self):
        return f'{self.username} initiate'


class Performer(models.Model):

    performed = models.BooleanField(default=False, verbose_name="Performer")
    initiator = models.BooleanField(Initaitor, default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.performed