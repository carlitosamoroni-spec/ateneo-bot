import os, telebot, threading
from flask import Flask
from google import genai

app = Flask(__name__)
@app.route('/')
def home(): return "Bot activo"

def run_flask(): app.run(host='0.0.0.0', port=10000)
threading.Thread(target=run_flask).start()

bot = telebot.TeleBot(os.getenv("TOKEN"))
client = genai.Client(api_key=os.getenv("GEMINI_KEY"))

@bot.message_handler(func=lambda m: True)
def respuesta(m):
    try:
        res = client.models.generate_content(model='gemini-2.5-flash', contents=m.text)
        bot.reply_to(m, res.text)
    except: bot.reply_to(m, "Error en el sistema")

print("Iniciando Bot...")
bot.infinity_polling()
