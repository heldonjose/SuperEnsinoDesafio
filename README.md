# Para executar o projeto 

## COnfigurações

```
$ git clone git@github.com:heldonjose/SuperEnsinoDesafio.git
$ cd SuperEnsinoDesafio
```

Crie  a venv, ative e instale as dependências:

```
$ virtualenv venv -p python3.8  #Pode utilizar qualquer outra versão acima da 8
$ source venv/bin/activate
(venv) $pip install -r requeriments.txt  // Observe que a venv está ativada no inicio da linha

```


Projeto utilizando o sqlite3,

Na raiz do projeto, execute:

```
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