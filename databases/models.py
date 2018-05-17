# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_profiles(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'user_info')
    name = models.CharField(max_length = 20)
    gender = models.CharField(max_length = 5)

class Events(models.Model):
    name = models.CharField(max_length = 100)
    team_max = models.DecimalField(decimal_places = 0, max_digits = 5)
    member_min = models.DecimalField(decimal_places = 0, max_digits = 3)
    time = models.DateTimeField()

class Teams(models.Model):
    name = models.CharField(max_length = 20)
    event_id = models.ForeignKey(Events, on_delete = models.DO_NOTHING)

class Teammembers(models.Model):
    team_id = models.ForeignKey(Teams, on_delete = models.DO_NOTHING)
    user_id = models.ForeignKey(User, on_delete = models.DO_NOTHING)

class Announcements(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 5000)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
