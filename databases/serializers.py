from rest_framework import serializers
from databases.models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.CharField(source = 'user_info.name')
    gender = serializers.CharField(source = 'user_info.gender')
    
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'name', 'gender')

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
    class meta:
        model = Announcements
        fields = '__all__'

