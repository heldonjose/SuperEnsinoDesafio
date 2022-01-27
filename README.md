# Para executar o projeto 

## COnfigurações

```
$ git clone git@github.com:heldonjose/challenge-ByCodersTec.git
$ cd challenge-ByCodersTec
```

Crie  a virtualenv, ative e instale as dependências:

```
$ virtualenv env
$ source env/bin/activate
(env) $pip install -r requirements.txt  // Note que a env está ativada no inicio da linha

```

Coloque as configuração do banco de dados post no arquivo settings na pasta projeto :
Lembre de colocar o nome do banco, usuário e password;
Caso queria utilizar o sqlite3, somente remover essas linhas do arquivo
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'challenge_byCoders',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432', }
}
```
Na raiz do projeto, execute:
Na raiz do projeto, execute:

```
(env)$ python manage.py createsuperuser
(env)$ python manage.py migrate
(env)$ python manage.py createsuperuser

```

POr fim, execute o projeto:
```
(env)$ python manage.py runserver
```
Navegue para `http://127.0.0.1:8000`.
Faça login com o usuário e senha criado.

Para acessar o admin do django, acesse: `http://127.0.0.1:8000/admin`.