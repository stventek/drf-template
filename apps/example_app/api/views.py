from apps.example_app.api.serializers import AuthorSerializer, BlogPostSerializer
from apps.example_app.models import Author, BlogPost
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    @action(detail=False, methods=['get'])
    def custom(self, request):
        return Response('custom view')