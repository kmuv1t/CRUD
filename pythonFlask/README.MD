#CRUD

Teste com CRUD usando flask e suas ferramentas

- Flask
- flask_alchemy
- flask_migrate
- flask_marshmallow
- marshmallow_sqlalchemy
- flask-jwt-extended

# Como rodar esse projeto:

```shell
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_Debug=True

flask run
```

# Migrações:

``sh
flask db init
flask db migrate
flaks db update
``