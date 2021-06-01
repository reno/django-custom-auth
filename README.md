# django-custom-auth

![](https://img.shields.io/pypi/pyversions/Django) ![](https://img.shields.io/travis/reno/django-custom-auth) ![](https://img.shields.io/coveralls/github/reno/django-custom-auth)

Um app reutilizável de autenticação de usuário para Django.

Este app tem como objetivo fornecer recursos básicos de cadastro e autenticação de usuário, utilizando ao máximo os recursos já inclusos no Django e sem dependências.


## 💭 Motivação

- **Django fornece boa parte da funcionalidade necessária para a manutenção de usuários**. A principal funcionalidade ausente, e motivação para este projeto, é a confirmação de email no cadastro de usuários.
- **Todos os demais recursos inclusos no Django são utilizados no app**: login/logout, mudança e reset de senha com envio de link único por email. Tudo que é necessário é fornecer os templates.
- **Adicionar campos ao modelo de usuário é uma necessidade frequente**. Este app estende o modelo de usuário do Django para incluir a confirmação de email, e um usuário customizado permite que campos adicionais sejam incluídos. 
- **Nenhum pacote de terceiros é necessário**, permitindo melhor customização e integração do app com o restante do seu projeto.



## 📌 Requisitos
- Python 3.6+
- pip
  

## ⚙️ Tecnologias utilizadas
- Django 3
  

## 🚀 Uso

Primeiramente, crie um ambiente virtual:

`python -m venv venv`

Ative o ambiente virtual:

`source venv/bin/activate`

Instale o Django

`pip install django`

Inicialize um projeto usando este repositório como template:

`django-admin startproject --template=https://github.com/reno/django-custom-auth/archive/master.zip <project_name> .`

Execute as migrações do banco de dados:

`python3 manage.py migrate`

Finalmente, execute o servidor de desenvolvimento:

`python manage.py runserver`


## 🎯 Testes

Para executar os testes, após ativar o ambiente virtual e instalar as dependências, execute o comando:

`python manage.py test`

