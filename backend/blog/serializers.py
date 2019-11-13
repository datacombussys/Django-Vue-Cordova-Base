from rest_framework import serializers
from blog.models import BlogModel
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ['id', 'author', 'title', 'content', 'date_posted', 'last_updated', 'slug']