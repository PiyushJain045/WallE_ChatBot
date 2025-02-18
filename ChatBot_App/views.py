from django.shortcuts import render
from django.views import View
import markdown

import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv() 

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")

# Create your views here.

class Home(View):
    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        return render(request, "home.html")
    

class Chat(View):
    def get(self, request):
        print("Inside chat get")
        return render(request, "chat.html")

    def post(self, request):
        print("Inside chat post")
        prompt = request.POST.get("field")
        print(prompt)

        response = model.generate_content(prompt)
        bot_response = markdown.markdown(response.candidates[0].content.parts[0].text)
        print(bot_response)

        chats = [
            {"role": "user", "text": prompt},
            {"role": "bot", "text": bot_response},
            
            
        ]

        return render(request, "partials/chat_messages.html", {"chats":chats})
    

class Theme(View):
    def get(self, request):
        pass

    def post(self, request):
        print("Inside theme post")
        theme_choice = request.POST.get("field-2")
        print("theme choice:",theme_choice)

        theme_image = f"themes/{theme_choice}.jpg"
        theme_video = f"themes/{theme_choice}.mp4"
        print(theme_video)

        return render(request, "partials/theme_partial.html", {
            "theme_image": theme_image,
            "theme_video": theme_video
        })
    

class Music(View):
    def get(self, request):
        pass

    def post(self, request):
        print("Inside Music post")
        music_choice = request.POST.get("field-2")
        print("choice:",music_choice)

        music_choice_path = f"music/{music_choice}.mp3"
        print("path:", music_choice_path)

        return render(request, "partials/music_partial.html", {"music_choice_path": music_choice_path})

