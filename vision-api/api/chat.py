from flask import request, jsonify, Response
import openai
import json
from openai import OpenAI

def chat():
    try:
        data=request.json
        formatted_messages=[
            {
                "role": "user",
                "content": "Eres un asistente llamado ScienceVision. Responde las preguntas de los usuario con claridad"
            }
        ]
        #evitar en la interfaz elementos que no nos gusten es necesario limpiar la interfaz
        for message in data['messages']:
            formatted_messages.append({
                "role": role["role"],
                "content": message["content"],	
            })
        #inicilizar el cliente de OpenAI 
        client=OpenAI()
        #generar la respuesta en streming en timepo real
        response= client.chat.completions.create(
            model='gpt-4o-mini',
            messages=formatted_messages,
            temperature=0.7,
            stream=True
        )
        #por cada pedazo de Token que viene de response
        for chunck in response:
            if chunk.choices[0].delta.content:
                yield f""
        
    except Exception as e:
        print(f"Chat reques failed:{str(e)}")
        return jsonify({
            "error": str(e),
            'status': 'error'
        }), 500