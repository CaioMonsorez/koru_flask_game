# app/routes.py

from app import app

@app.route('/')
def index():
    return "Olá, mundo!"