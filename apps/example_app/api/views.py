from apps.core.filter import AnyModelFilter
from apps.example_app.api.serializers import AuthorSerializer, BlogPostSerializer
from apps.example_app.models import Author, BlogPost
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from django_filters import rest_framework as filters

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BlogPostFilter(AnyModelFilter):
    class Meta:
        model = BlogPost
        fields = '__all__'

class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    filterset_class  = BlogPostFilter

    @action(detail=False, methods=['get'])
    def custom(self, request):
        return Response('custom view')