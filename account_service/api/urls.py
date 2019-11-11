from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('login', views.LoginAPIView.as_view()),
    path('register', views.RegisterAPIView.as_view()),
    path('profile', views.ProfileAPIView.as_view()),
    path('change-password', views.ChangePasswordAPIView.as_view()),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
