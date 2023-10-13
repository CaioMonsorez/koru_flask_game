# data.py

# Dicionário de personagens
personagens = {
    1: {
        'nome': 'Markin',
        'classe': 'Padrão',
        'nivel': 10,
        'vida': 100,
        'ataque': 20,
        'imagem': 'https://media.tenor.com/x1eW6Z7pMnIAAAAi/animated-man-running.gif'

    },
    2: {
        'nome': 'Jorelei',
        'classe': 'Nerd',
        'nivel': 8,
        'vida': 80,
        'ataque': 25,
        'imagem': 'https://media.tenor.com/iPWC0upqq_QAAAAi/animated-man-running.gif'       

    },
    3: {
        'nome': 'Romil',
        'classe': 'Atacante',
        'nivel': 12,
        'vida': 90,
        'ataque': 18,
        'imagem': 'https://64.media.tumblr.com/efa9c31a801e7c54c62c37289d881c69/tumblr_mrw6ovcjPW1rfjowdo1_500.gif'
    },
     4: {
        'nome': 'Nelly',
        'classe': 'Millenium',
        'nivel': 80,
        'vida': 90,
        'ataque': 98,
        'imagem': 'https://cdna.artstation.com/p/assets/images/images/044/949/056/original/pedro-manuel-correia-pereira-samurai-1-direita-andar-atacar.gif'
    },
    5: {
        'nome': 'Tofu',
        'classe': 'Samurai',
        'nivel': 80,
        'vida': 90,
        'ataque': 98,
        'imagem': 'https://cdna.artstation.com/p/assets/images/images/044/949/082/original/pedro-manuel-correia-pereira-samurai-2-direita-ataque.gif'
    },
    6: {
        'nome': 'Zumbi',
        'classe': 'Morto',
        'nivel': 80,
        'vida': 90,
        'ataque': 98,
        'imagem': 'https://i.pinimg.com/originals/a6/21/0f/a6210fd59c68852a3143ccde924e6cf2.gif'
    },
    7: {
        'nome': 'Goku',
        'classe': 'Saiyajin',
        'nivel': 85,
        'vida': 95,
        'ataque': 94,
        'imagem': 'https://i.gifer.com/origin/38/38fe168959a1c6ad51693c7e028389e0_w200.gif'
    },
    8: {
        'nome': 'Piccolo',
        'classe': 'Saiyajin',
        'nivel': 82,
        'vida': 96,
        'ataque': 92,
        'imagem': 'https://media.tenor.com/XscLOxYAmbMAAAAj/dragonball-sprite.gif'
    },
    9: {
        'nome': 'Bills',
        'classe': 'Saiyajin',
        'nivel': 87,
        'vida': 94,
        'ataque': 92,
        'imagem': 'https://media.tenor.com/pbx_WkDZpQcAAAAj/beerus-dbz.gif'
    },
    10: {
        'nome': 'Naruto',
        'classe': 'Ninja',
        'nivel': 85,
        'vida': 95,
        'ataque': 94,
        'imagem': 'https://images.gamebanana.com/img/ico/sprays/naruto.gif'
    },
    11: {
        'nome': 'Sasuke',
        'classe': 'Ninja',
        'nivel': 90,
        'vida': 92,
        'ataque': 96,
        'imagem': 'https://images.gamebanana.com/img/ico/sprays/sasuke.gif'
    },
    12: {
        'nome': 'Sakura',
        'classe': 'Ninja',
        'nivel': 89,
        'vida': 93,
        'ataque': 97,
        'imagem': 'https://images.gamebanana.com/img/ico/sprays/sakura-running.gif'
    },
    # Adicione mais personagens aqui, se necessário
}

#---------------------------------------------------------------------------------------------------------------
# 1.FUNÇÕES CRUD:
# Script para simular funcionalidades do banco de dados.

# 1.1 FUNÇÃO PARA GERAR PERSONAGEM COM O PRÓXIMO ID DO DICIONÁRIO
def gerar_id():
  id = len(personagens) + 1
  return id
#---------------------------------------------------------------------------------------------------------------
# 1.2 FUNÇÃO PARA CRIAR PERSONAGEM
def criar_personagem(nome, classe, nivel, vida, ataque, imagem):
  personagens[gerar_id()] = {"nome":nome, "classe":classe, "nivel":nivel, "vida":vida, "ataque":ataque, "imagem":imagem}

# 1.3 FUNÇÃO PARA ATUALIZAR DADOS DO PERSONAGEM
def atualizar_personagem(id, dados_personagem:dict):
  personagens[i] = dados_personagem

# 1.4 FUNÇÃO PARA REMOVER UM PERSONAGEM
def remover_personagem(id:int):
  del personagens[id]

#---------------------------------------------------------------------------------------------------------------
# 1.5 FUNÇÃO RETORNAR UM ÚNICO PERSONAGEM
def retornar_personagem(id:int):
  if id in personagens.keys():
    return personagens[id] 
  else:
    return {}
  
# 1.6 FUNÇÃO PARA RETORNAR TODOS OS PERSONAGENS
def retornar_personagens():
  return personagens




