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
        try:
            return render(request, "home.html")
        except Exception as e:
            error_message = str(e)
            return render(request, 'error/error.html', 
                          {'error_message': error_message,
                           'status_code':500})


    def post(self, request):
        try:
            return render(request, "home.html")
        except Exception as e:
            error_message = str(e)
            return render(request, 'error/error.html', 
                          {'error_message': error_message,
                           'status_code':500})

    

class Chat(View):
    def get(self, request):
        try:
            print("Inside chat get")
            return render(request, "chat.html")
        except Exception as e:
            error_message = str(e)
            return render(request, 'error/error.html', 
                          {'error_message': error_message,
                           'status_code':500})


    def post(self, request):
        try:
            if request.user.is_authenticated:
                user_name = request.user.username
                print(user_name)
            else:
                user_name = ""

            print("Inside chat post")

            user_message = request.POST.get("field")
            prompt = f"I am using you in my chatbot application called Wall-E, so your name is now Wall-E. The prompts you receive will be from users. Your goal is to keep the conversation as friendly and concise as possible. Use the user's name frequently to make the conversation more immersive. The user's name is {user_name}. That's all. Now, here is the user's prompt: {user_message}"
            print(prompt)

            if request.user.is_authenticated:
                user_name = request.user.username
            else:
                user_name = ""

            response = model.generate_content(prompt)
            bot_response = markdown.markdown(response.candidates[0].content.parts[0].text)
            print(bot_response)

            chats = [
                {"role": "user", "text": user_message},
                {"role": "bot", "text": bot_response},
                
                
            ]

            return render(request, "partials/chat_messages.html", {"chats":chats})
        
        except Exception as e:
            error_message = str(e)
            return render(request, 'error/error.html', 
                          {'error_message': error_message,
                           'status_code':500})

    
    

class Theme(View):
    def get(self, request):
        pass

    def post(self, request):
        try:
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
        except Exception as e:
            error_message = str(e)
            return render(request, 'error/error.html', 
                          {'error_message': error_message,
                           'status_code':500})

    

class Music(View):
    def get(self, request):
        pass

    def post(self, request):
        try:
            print("Inside Music post")
            music_choice = request.POST.get("field-2")
            print("choice:",music_choice)

            music_choice_path = f"music/{music_choice}.mp3"
            print("path:", music_choice_path)

            return render(request, "partials/music_partial.html", {"music_choice_path": music_choice_path})
        except Exception as e:
            error_message = str(e)
            return render(request, 'error/error.html', 
                          {'error_message': error_message,
                           'status_code':500})


