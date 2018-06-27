# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User_profiles(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'profile')
    name = models.CharField(max_length = 50, default='noname')
    gender = models.IntegerField(default = 0)
    role_id = models.IntegerField(default = 0)

class Events(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(default = 'qaq')
    rule = models.TextField(default = 'qaq')
    status = models.IntegerField(default = 0)
    excerpt = models.TextField(default = 'qaq')
    team_max = models.IntegerField(default = 10)
    member_min = models.IntegerField(default = 1)
    regist_start = models.DateTimeField(default=datetime.now, blank=True) 
    regist_end = models.DateTimeField(default=datetime.now, blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(default=datetime.now,blank = True)

class Teams(models.Model):
    name = models.CharField(max_length = 30)
    event_id = models.ForeignKey(Events, on_delete = models.CASCADE)
    vertify = models.BooleanField(default = False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True,blank = True)

class Teammembers(models.Model):
    team_id = models.ForeignKey(Teams, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)

class Announcements(models.Model):
    title = models.CharField(max_length = 60)
    description = models.TextField(default = 'qaq')
    user_id = models.IntegerField(default = 0)
    status = models.IntegerField(default = 0)
    announce_start = models.DateTimeField(default=datetime.now, blank=True)
    announce_end = models.DateTimeField(default=datetime.now, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
