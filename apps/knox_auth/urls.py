from django.urls import path
from . import views
from knox.views import LogoutView, LogoutAllView

urlpatterns = [
    path('login/', views.LoginAPIView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('logout-all/', LogoutAllView.as_view()),
]