# GRADE DE PROGRAMAÇÃO

Construa uma API REST em Django, que será responsável por entregar a grade de programação das rádios e alimentar o conteúdo dos sites e Apps do SGR.

# Regras:
### API deve retornar 
 - o programa que está no ar no momento,
 - a lista de programas de cada rádio,
 - a grade de programação de cada rádio.
 - caso exista algum jogo de futebol programado, ele deverá ter prioridade sobre o programa cadastrado no mesmo horário.
 
 
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
 make install
```

# Administrador (CMS):
1. Para Publicação e gerenciamento dos programas basta acessar http://meuIp/admin
acessar: 
- usuário: admin
- senha: admin

2. Primeiro deve-se cadastrar uma rádio com seus respectivos programas acessando:  http://meuIp/admin/radio/radio/
3. Depois acessar http://meuIp/admin/radio/grade/ para criar a grade de programação desta nova rádio.
4. Logo depois acessar os endpoins para obter informações e dados do sistema de conteúdo.

# Endpoints:

#### 1. lista de todos os endpoins do sistema de rádio;  
	
  - /api/

#### 2. programa que está no ar no momento;
	
  - /api/programa-atual/
  - /api/programa-atual/{id_radio}/

#### 3. lista de programas de cada rádio;  
	
  - /api/radio/
  - /api/radio/{id_radio}/
 
#### 4. grade de programação de cada rádio;  
	
  - /api/grade/
  - /api/grade/{id_radio}/

## Apps
 
### radio
- Responsável por concentrar todas as configurações ralacionadas a grade de programação.
- models, views, serializers



### core
- Responsável por concentrar todas as configurações relacionadas a segurança e autenticação de usuário da API.


### api
- Responsável por concentrar todas as configurações relacionadas aos endpoints da API REST


## Observações

- A aplicação core detém configurações para autenticação via REST API e segurança dos endpoins via Token.
- Desconsiderar a aplicação apps.core
- Os testes eu me concentrei apenas em alguns BDD's para testar o comportamento dos endpoins.