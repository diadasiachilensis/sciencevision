from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import openai
import os
from app.api.chat import chat 

def create_app():
    #carga las variables del entorno
    load_dotenv()
    #inicializa la aplicacion flask 
    app=Flask(__name__)
    #permite todos los origenes con la configuracion predeterminada
    CORS(app)
    #registra las rutas directamente
    app.add_url_rule('/api/chat','chat',chat,methods={'POST'})

    return app
