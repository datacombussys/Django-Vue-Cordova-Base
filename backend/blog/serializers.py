from django.contrib.auth.models import User, Group
from rest_framework import serializers
from blog.models import BlogModel
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ['id', 'author', 'title', 'content', 'date_posted', 'last_updated', 'slug']