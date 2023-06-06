from django.urls import include, path
from rest_framework import routers

from apps.example_app.api.views import AuthorViewSet, BlogPostViewSet

router = routers.DefaultRouter()

router.register(r'blog_post', BlogPostViewSet)
router.register(r'author', AuthorViewSet)

urlpatterns = [
    path('', include(router.urls), ),
]