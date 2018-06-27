from rest_framework import serializers
from databases.models import *
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text



class UserSerializer(serializers.HyperlinkedModelSerializer):
    userid = serializers.IntegerField(source = 'profile.pk',read_only=True)

    class Meta:
        model = User
        fields = ('id','username', 'email', 'password','is_active', 'userid')
        extra_kwargs = {'password': {'write_only': True}, 'id':{'read_only':True}}
    
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            is_active=validated_data['is_active']
        )
        user.set_password(validated_data['password'])
        user.save()
        mail_subject = 'Activate your account.'
        message = render_to_string('acc_active_email.html',{
            'user':user,
            'domain':'www.hy0936.com.tw:9990',
            'uid':user.pk,
            'token':account_activation_token.make_token(user),
        })
        to_email = user.email
        email = EmailMessage(
            mail_subject,
            message,
            to=[to_email]
        )
        email.send()

        return user


    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class User_profilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_profiles
        fields = '__all__'

class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'

class TeammembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teammembers
        fields = '__all__'

class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

class AnnouncementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcements
        fields = '__all__'

#class UserdataSerializer(serlizers.)


