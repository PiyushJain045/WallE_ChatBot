from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path("Chatting", views.Chat.as_view(), name='chat'),
]