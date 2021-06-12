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

## Register new user
``` curl -X POST http://127.0.0.1:8000/api/register/ -H "Content-Type: application/json" -d '{"username":"{CHOOSE USERNAME}", "password":"{CHOOSE PASSWORD}", "email":"{YOUR EMAIL}"}'```

Response:
```{"user":{"id":11,"username":"gustavo","email":"camagrock@gmail.com"},"token":"a8c622797004e552499db37580db880753b226050272095a9e511ef338a6a77b"}```
Store the user **id** and **token** in order to use it on CRUD operations
## Login
```curl -X POST http://127.0.0.1:8000/api/login/ -H "Content-Type: application/json" -d '{"username":"{YOUR USERNAME}", "password":"{YOUR PASSWOR}"}' ```

Response:
``` {"expiry":"2021-06-12T04:15:46.999588Z","token":"e17ec773d72111dcf17847bdab88fdcf51680509b21d76a2f37911708e25e6b7"} ```
Store the **token** in order to use it on CRUD operations

## Logout
``` curl -X POST http://127.0.0.1:8000/api/logout/ -H 'Authorization: Token {token from login return json}'```

## List User Tasks
```curl -X GET http://127.0.0.1:8000/api/ -H 'Authorization: Token {token from login return json}'```

Response:

``` [{"id":8,"task_name":"pass itv","is_completed":false,"date_of_creation":"2021-06-08T15:39:18.907695Z","user":5},{"id":46,"task_name":"finish FluToDo","is_completed":true,"date_of_creation":"2021-06-10T15:06:45.059771Z","user":5}] ``` 

Store the task **id** for update and delete operations  

## Create new task
```curl -X POST http://127.0.0.1:8000/api/create/ -H "Content-Type: application/json" " Authorization: Token a8c622797004e552499db37580db880753b226050272095a9e511ef338a6a77b" -d '{ "task_name": "{CHOOSE TASK NAME}" , "user": {USER ID FROM REGISTER RESPONSE} }' ```

## Update task

```curl -XPATCH -H 'Content-Type:application/json' -H "Authorization: Token {token from login return json}"  -d '{"is_completed": {true|false} }' http://127.0.0.1:8000/api/update/{TASK_ID}```

## Delete task

```curl -X DELETE "http://127.0.0.1:8000/api/delete/{TASK_ID}" -H "Authorization: Token 426d8b8a5337a3d6fbfb75f7c12f7206a9141679ccea39500dff0f2a4e6aec78"```


