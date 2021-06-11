# How to run FluToDo



# Boot Docker
```docker-compose up```

# Install requirements
```docker-compose exec web pip3 install -r requirements.txt```

# Migrate models
```docker-compose exec web python manage.py makemigrations```

```docker-compose exec web python manage.py migrate```

# Activate virtualevn 
```source venv/bin/activate```

# Migrate django-rest-knox models
```python manage.py migrate```

# API endpoints on localhost

## Create User

## Login
```curl -X POST http://127.0.0.1:8000/api/login/ -H "Content-Type: application/json" -d '{"username":"{YOUR USERNAME}", "password":"{YOUR PASSWOR}"}' ```

The response will be like:
``` {"expiry":"2021-06-12T04:15:46.999588Z","token":"e17ec773d72111dcf17847bdab88fdcf51680509b21d76a2f37911708e25e6b7"} ```
Store the token in order to use it on CRUD operations

## Logout
``` curl -X POST http://127.0.0.1:8000/api/logout/ -H 'Authorization: Token {token from login return json}'```

## List User Task
```curl -X GET http://127.0.0.1:8000/api/ -H 'Authorization: Token {token from login return json}'```
