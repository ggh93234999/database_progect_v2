# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User

from databases.models import *
from databases.serializers import *

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class User_profilesViewSet(viewsets.ModelViewSet):
    queryset = User_profiles.objects.all()
    serializer_class = User_profilesSerializer

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class TeamsViewSet(viewsets.ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer

class TeammembersViewSet(viewsets.ModelViewSet):
    queryset = Teammembers.objects.all()
    serializer_class = TeammembersSerializer

class AnnouncementsViewSet(viewsets.ModelViewSet):
    queryset = Announcements.objects.all()
    serializer_class = AnnouncementsSerializer

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from databases.models import User_profiles

def Signup(request):
    
    if request.method == 'POST':
        try:
            print('in post QQQQ')

            uname = request.POST['username']
            upass = request.POST['password']
            umail = request.POST['email']
            rname = request.POST['name']
            rgender = request.POST['gender']
            print(uname,upass,umail,rname)
            tmp_new_user = User.objects.create_user(uname,umail,upass)
            print(tmp_new_user.id)
            tmp = User_profiles(user = tmp_new_user, name = rname, gender = rgender)
            print(tmp)
            tmp.save()
            return HttpResponse("Create Successful")

        except:
            response = HttpResponse("Something Error")
            response.status_code = 400
            return response




#===============after here is test================
#@api_view(['GET'])i
#def UserViewSer(request)
#    if request.method == 'GET':
#        Uset = User_profiles.objects.all()
#        Rset = User.objects.all()
#        serializer = UserSerializer()



