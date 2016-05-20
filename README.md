# Sigma

Implementação do trabalho de Projetos de Sistema.

## Instalação e funcionamento

Para instalar o projeto, e iniciar o servidor de debug, você precisa instalar o Python 3, e a utilidade 'pip' (já vem com o Python 3.4). E então, execute os comandos seguintes em um terminal:

```bash
$ git clone https://github.com/possatti/bsi-ps-sigma sigma
$ cd sigma
$ pip install -r requirements.txt  # Instala o Django.
$ python manage.py migrate  # Cria as tabelas no BD.
$ python manage.py createsuperuser  # Entre com o nome e senha para o novo adminsitrador.
$ python manage.py runserver  # Inicia o servidor.
```
