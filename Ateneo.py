import os
import telebot
from google import genai
from google.genai import types

# TICKET Y KEY
TOKEN = "8831948080:AAEhkyKNLStLdIIbZRmy_-UZpYYx-9wquMg"
GEMINI_KEY = os.getenv("GEMINI_KEY")

client = genai.Client(api_key=GEMINI_KEY)
bot = telebot.TeleBot(TOKEN)

PROMPT_ATENEO = "Eres Ateneo, un asistente intelectual..." # Pegá acá tu prompt

@bot.message_handler(func=lambda m: True)
def respuesta(m):
    try:
        respuesta = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=m.text,
            config=types.GenerateContentConfig(system_instruction=PROMPT_ATENEO, temperature=0.5)
        )
        bot.reply_to(m, respuesta.text)
    except:
        bot.reply_to(m, "Error en el sistema.")

bot.infinity_polling()
