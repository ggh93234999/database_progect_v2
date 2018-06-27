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
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.core.mail import EmailMessage
from django.core.mail import send_mail

# Create your views here.

def activate(request, uidb64, token):
    try:
        uid = uidb64
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')

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
    
    def update(self, request, pk=None):
        team = self.get_object()
        serializer = TeamsSerializer(team, data = request.data)
        if serializer.is_valid():
            serializer.save()
            try:
                if serializer.data['vertify']:
                    teamid = serializer.data['id']
                    da = Teammembers.objects.filter(team_id=teamid)
                    se = TeammembersSerializer(da, many = True)
                    emails=[]
                    for i in se.data:
                        us = User.objects.get(pk=i['user_id'])
                        se_us = UserSerializer(us)
                        emails.append(se_us.data['email'])
                    print(emails)
                    send_mail(
                        'event register successful',
                        'good good be good',
                        '<nctudatabase@gmail.com>',
                        emails
                    )
            except:
                print("some one not good");
            return Response(serializer.data)
        return Response(serializer,errors, status = status.HTTP_400_REQUEST)

class TeammembersViewSet(viewsets.ModelViewSet):
    queryset = Teammembers.objects.all()
    serializer_class = TeammembersSerializer

class AnnouncementsViewSet(viewsets.ModelViewSet):
    queryset = Announcements.objects.all()
    serializer_class = AnnouncementsSerializer


