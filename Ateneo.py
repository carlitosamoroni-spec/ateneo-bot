import os
import telebot
from google import genai
from google.genai import types
from flask import Flask
from threading import Thread
import time

# Configuración del servidor web
app = Flask(__name__)
@app.route('/')
def home():
    return "Bot activo"

def run():
    app.run(host='0.0.0.0', port=10000)

# Iniciamos el servidor en segundo plano
Thread(target=run).start()

# Configuración del Bot
TOKEN = os.getenv("TOKEN")
GEMINI_KEY = os.getenv("GEMINI_KEY")

client = genai.Client(api_key=GEMINI_KEY)
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda m: True)
def respuesta(m):
    try:
        resultado = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=m.text,
        )
        bot.reply_to(m, resultado.text)
    except Exception as e:
        bot.reply_to(m, "Error en el sistema")

print("Iniciando Bot...")
bot.infinity_polling(skip_pending=True)
