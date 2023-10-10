# personagens.py
from flask import Flask, render_template
from PIL import Image
from data import personagens

app = Flask(__name__)

@app.route('/')
def index():
    return "Página Inicial do Jogo"

@app.route('/personagens')
def listar_personagens():
    return render_template('personagens.html', personagens=personagens)


if __name__ == '__main__':
    app.run(debug=True)
