from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum

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
    officer = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    candidate_one = models.IntegerField(blank=True, null=True)
    candidate_two = models.IntegerField(blank=True, null=True)
    candidate_three = models.IntegerField(blank=True, null=True)
    candidate_four = models.IntegerField(blank=True, null=True)
    totalvotes = models.IntegerField(blank=True, null=True)
    rejectedvotes = models.IntegerField(blank=True, null=True)
    validvotes = models.IntegerField(blank=True, null=True)
    regvoters = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.officer)+ " " + str(self.candidate_one) + " " + str(self.candidate_two) + " " + str(self.candidate_three) + " " + str(self.candidate_four) + " " + str(self.totalvotes) + " " + str(self.rejectedvotes) + " " + str(self.validvotes) + " " + str(self.regvoters)




class Candidate(models.Model):
    candidate_name = models.CharField(max_length=30, blank=True)
    candidate_image = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    candidate_party = models.CharField(max_length=60, blank=True)
    party_logo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    

    def __str__(self):
        return self.candidate_name
