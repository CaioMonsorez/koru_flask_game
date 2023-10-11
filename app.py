# personagens.py
from flask import Flask, render_template, request, jsonify
from data import personagens

app = Flask(__name__)

# Variáveis para a posição do caminhão
truck_x = 100
truck_y = 100

# Variável para a pontuação
score = 0

# Define a cor de fundo
background_color = "lightblue"

@app.route('/jogo')
def iniciar_jogo():
    return render_template('jogo.html', truck_x=truck_x, truck_y=truck_y, background_color=background_color, score=score)

@app.route('/move_truck', methods=['POST'])
def move_truck():
    global truck_x, truck_y, score

    direction = request.json['direction']
    step = 10

    if direction == 'left':
        truck_x -= step
    elif direction == 'right':
        truck_x += step
    elif direction == 'up':
        truck_y -= step
    elif direction == 'down':
        truck_y += step

    # Atualizar a pontuação (por exemplo, +10 a cada movimento)
    score += 10

    return jsonify({'truck_x': truck_x, 'truck_y': truck_y, 'score': score})

@app.route('/reset_game', methods=['POST'])
def reset_game():
    global truck_x, truck_y, score

    # Reiniciar a posição do caminhão e a pontuação
    truck_x = 100
    truck_y = 100
    score = 0

    return jsonify({'truck_x': truck_x, 'truck_y': truck_y, 'score': score})

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/personagens')
def listar_personagens():
    return render_template('personagens.html', personagens=personagens)

if __name__ == '__main__':
    app.run(debug=True)
