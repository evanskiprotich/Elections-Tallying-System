from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    ADMIN = 1
    OFFICER = 2
    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (OFFICER, 'Officer'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    county = models.CharField(max_length=30, blank=True)
    county_code = models.IntegerField(null=True)
    constituency = models.CharField(max_length=30, blank=True)
    constituency_code = models.IntegerField(null=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, null=True, blank=True)

    def __str__(self): 
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

class Result(models.Model):
    officer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    candidate1 = models.IntegerField()
    candidate2 = models.IntegerField()
    candidate3 = models.IntegerField()
    candidate4 = models.IntegerField()
    valid_votes = models.IntegerField()
    rejected_votes = models.IntegerField()
    registered_voters = models.IntegerField()

    def __str__(self):
        return str(self.candidate1) + " " + str(self.candidate2) + " " + str(self.candidate3) + " " + str(self.candidate4) 

#user model with username, first name, last name, county, county code, constituency, constituency code
# class User(models.Model):
#     username = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     county = models.CharField(max_length=100)
#     county_code = models.CharField(max_length=100)
#     constituency = models.CharField(max_length=100)
#     constituency_code = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.username + ' ' + self.first_name + self.last_name + self.county + self.county_code + self.constituency + self.constituency_code
