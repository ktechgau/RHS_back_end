from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Profile(models.Model):
  owner = models.OneToOneField(
    get_user_model(),
    on_delete=models.CASCADE,
    primary_key=True,
    related_name='user_profile')
  # first_name = models.CharField(max_length=30,null=False, blank=False)
  # last_name = models.CharField(max_length=30,null=False, blank=False)
  # username = models.CharField(max_length=30,null=False, blank=False)
  bio = models.CharField(max_length=1800, null=False, blank=False)
  location = models.CharField(max_length=50,null=True, blank=True)
  picture_url = models.URLField(null=True, blank=True)
  is_hidden = models.BooleanField(null=True, blank=True)
  number_of_endorsements = models.IntegerField(null=True, blank=True)
  email_url = models.EmailField(null=True, blank=True)
  facebook_url = models.URLField(null=True, blank=True)
  instagram_url = models.URLField(null=True, blank=True)
  github_url = models.URLField(null=True, blank=True)
  linkedin_url = models.URLField(null=True, blank=True)
  portfolio_url = models.URLField(null=True, blank=True)
  contact_preference_choices = (
        ("Contact Form", "Contact Form"),
        ("Email", "Email"),
        ("LinkedIn", "LinkedIn"),
        ("Facebook", "Facebook"),
        ("Instagram", "Instagram")
    )
  contact_preference = models.CharField(max_length=30, choices=contact_preference_choices, default="Email")
  is_open_to_mentor = models.BooleanField(null=True, blank=True)
  is_seeking_mentorship = models.BooleanField(null=True, blank=True)
  date_created = models.DateTimeField(null=True, blank=True)

  