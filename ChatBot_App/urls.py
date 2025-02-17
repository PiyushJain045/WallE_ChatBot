from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path("Chatting", views.Chat.as_view(), name='chat'),
    path("change_theme", views.Theme.as_view(), name='theme'),
    path("change_music", views.Music.as_view(), name='music')
]