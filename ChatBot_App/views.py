from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View

# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        return render(request, "home.html")
    

class Chat(View):
    def get(self, request):
        return render(request, "chat.html")

    def post(self, request):
        return render(request, "home.html")