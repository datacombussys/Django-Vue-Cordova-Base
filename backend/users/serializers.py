# from .models import Profile, Team
from rest_framework import serializers
from users.models import Users
from users.common-models import CommonGroup


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')


# class TeamSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Team
#         fields = ('name', 'description',)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommonGroup
        fields = ['url', 'name']
