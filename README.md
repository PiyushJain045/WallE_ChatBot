- [Wall-E Chatbot](https://walle-chatbot.onrender.com/) | Note: not optimized for mobile

# 🤖 Wall-E Chatbot

Wall-E is a friendly AI chatbot built with Django and powered by the **Gemini-Flash API**. Inspired by the charming character from the movie "WALL·E", this chatbot offers an immersive, personalized experience with customizable themes and background music.

---

## 🚀 Features

- 🎨 **Theme Customization**: Users can switch between different visual themes (light/dark/space).
- 🎵 **Background Music**: Enjoy ambient music while chatting. You can turn it on/off based on your preference.
- 🧠 **Smart AI Conversations**: Integrated with Gemini-Flash API for intelligent, contextual responses.
- 🙋 **Personalized Greetings**: If the user is logged in, Wall-E remembers and uses their name in replies.
- 💬 **Interactive Chat Interface**: Real-time chatting experience using Django views and templates.

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Webflow, HTMX 
- **AI Integration**: Gemini Flash API
- **Authentication**: Django built-in auth system
- **Hosting**: Render / Localhost

---

### Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/PiyushJain045/WallE_ChatBot.git
   cd WallE_ChatBot

2. **Setup a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt

4. ** Add Your Gemini API key in .env file **:
   ```bash
   GEMINI_API_KEY="Add your gemini-1.5-flash API key"

5. **Run Migrations**:
   ```bash
   python manage.py makemigration
   python manage.py migrate

6. **Start the Development Server**:
   ```bash
   python manage.py runserver

**And voilà! Your setup is complete.** 🎉  

**Thanks for checking out this repo!** 🙌  

