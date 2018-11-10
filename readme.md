# GRADE DE PROGRAMAÇÃO

Construa uma API REST em Django, que será responsável por entregar a grade de programação das rádios e alimentar o conteúdo dos sites e Apps do SGR.

Rules:
 - O programa que está no ar no momento,
 - A lista de programas de cada rádio,
 - A grade de programação de cada rádio.
 - Caso exista algum jogo de futebol programado, ele deverá ter prioridade sobre o programa cadastrado no mesmo horário.
 
 
# Requesitos
 - Python 3
 - Django 2
 
# Como instalar

 1. clone o repositório.
 2. crie um virtualenv com o Python 3. (https://virtualenv.pypa.io/en/stable/)
 3. ative virtualenv.
 4. instale as dependências. (pip install -r requirements.txt)
 5. executar o projeto.
 
 ```console
 git clone https://github.com/asafepy/crawler-challenge.git
 cd desafio-sgr
 virtualenv -p python3 .virtualenv
 source .virtualenv/bin/activate
 pip install -r requirements.txt
 make test
 make seed
 make serve
```

# Endpoints:

1. lista de todos os endpoins da rádio;  
	- /api/

2. programa que está no ar no momento;
	- /api/programa-atual/{id_radio}/

3. lista de programas de cada rádio;  
	- /api/grade-programacao/
 
4. grade de programação de cada rádio;  
	- /api/grade-programacao/{id_radio}
        
## Apps
 
### radio
- Responsável por concentrar todas as configurações ralacionadas a grade de programação.
- models, views, serializers



### core
- Responsável por concentrar todas as configurações relacionadas a segurança e autenticação de usuário da API.


### api
- Responsável por concentrar todas as configurações relacionadas aos endpoints da API REST