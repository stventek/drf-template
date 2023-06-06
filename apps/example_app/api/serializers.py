from rest_framework import serializers
from django.contrib.auth.models import User

from apps.example_app.models import Author, BlogPost

class AuthorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Author
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'