from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    """
    Primary object for logging into the site.
    Extends the User object via one-to-one -connection.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The following details can be found from User Model:
    # first_name
    # last_name
    # email
    # password
    # is_superuser
    # date_joined
    # last_login
    description = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=255, blank=False)
    birthdate = models.DateField(null=True, blank=True)
    #websitetheme = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return "(ID = " + str(self.pk) + ") Profile: " + self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        # TODO
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        # TODO
        instance.profile.save()
