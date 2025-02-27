from flask import Flask, request, jsonify, send_file
from groq import Groq
from flask_cors import CORS
from flask_cors import cross_origin
from app.controller.chatbot import chatbot
from app.controller.text_to_speech import generate_audio
from app.controller.text_to_image import generate_image
from app.services.text_to_image_service import text_to_image
import asyncio

from gtts import gTTS
import os

from app.services.chatbot_service import chat_with_bot


# Tạo ứng dụng Flask
app = Flask(__name__)
CORS(app)


# Endpoint API
@app.route("/chatbot", methods=["POST"])
def chat():
    return chatbot()


@app.route("/text-to-speech", methods=["POST"])
def speech():
    return generate_audio()


@app.route("/text-to-image", methods=["POST"])
def image():
    return generate_image()


# Chạy ứng dụng Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
