###### **09/10/2023**

***O que foi feito ?***

* Certifique-se de que o Python esteja instalado corretamente em seu sistema e esteja funcionando sem problemas.

```
python --version
```

* Verifique se o `pip` (gerenciador de pacotes Python) está funcionando corretamente.

`pip --version`

* Se o `pip` estiver desatualizado, atualize-o usando o seguinte comando:

```
pip install --upgrade pip
```

* **Instalar o Flask em um Ambiente Virtual** : Às vezes, problemas de instalação podem ocorrer devido a conflitos entre pacotes ou configurações do sistema. É uma boa prática criar um ambiente virtual para seus projetos Python. Crie um ambiente virtual e tente instalar o Flask dentro dele:

```
python -m venv venv
venv\Scripts\activate
pip install Flask
```

* Realizado a verificação se o framework Flask está na lista do python

```
pip list
```

* Ativar o Ambiente Virtual:

```
source venv/bin/activate

```

* Criado o controle de versão apenas dos arquivos de código-fonte e das dependências do seu projeto

```
pip freeze > requirements.txt

```

------------------------------------------------       ESTRUTURA DO PROJETO  -----------------------------------------------------

my-flask-app
   ├── static/
   │   └── css/
   │       └── main.css
   ├── templates/
   │   ├── index.html
   │   └── student.html
   ├── data.py
   └── students.py

* `static/`: Esta pasta é usada para armazenar arquivos estáticos, como folhas de estilo CSS, JavaScript e imagens. No caso,  já tem uma subpasta `css/` para armazenar seu arquivo `main.css`.		,
* `templates/`: Aqui é onde  deve colocar seus modelos HTML e pode renderizar esses modelos nas rotas apropriadas em seu aplicativo Flask.
* `data.py` e `students.py`: Esses arquivos define suas classes e lógica relacionada aos dados do seu aplicativo, como modelos de dados e funções de manipulação de dados.
* **Criação de rotas** - definir como as diferentes URLs do seu aplicativo web serão tratadas. As rotas são mapeadas para funções de view, que são responsáveis por processar as solicitações HTTP e retornar respostas.

1. **Importar o Flask** : Primeiro, você precisa importar a classe `Flask` do módulo `flask` no seu arquivo, normalmente chamado de `app.py` ou `__init__.py`, que serve como o ponto de entrada do seu aplicativo Flask.

```
from flask import Flask

```

2. C**riar uma instância do Flask** : Em seguida,  criar uma instância da classe `Flask` para representar seu aplicativo.

```

app = Flask(__name__)

```

---

**10/10/2023**



Para rodar o projeto vá até a raiz do projeto e execute:

```
python personagens.py
```

O projeto vai executar no server:

http://127.0.0.1:5000/personagens
