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
Navegue para `http://127.0.0.1:8000/admin/`.
Faça login com o usuário e senha criado, você irá ser redirecionado para a tela de admin do django.

Acesse a área academica e crie um novo exame
```
http://127.0.0.1:8000/academic/exam/ #Lista de Exames
http://127.0.0.1:8000/academic/exam/add/  #criar um novo exame

Crie um exame com a situação em rascunho.
Um exame só poderá ser retornar no endpoint se o mesmo estiver ativo.
Para ativar um exame:
     - Pelo menos 1 questão deverá ser criada;
     - Cada questão deverá ter pelo menos 1 opção;
     - Cada questão deverá ter pelo menos 1 opção marcada como correta 
```
 
Para acessar a aŕes da documentação dos endpoint, acesse:

```
http://127.0.0.1:8000/swagger/
NO parametro de versão, colocar sempre o v1
```