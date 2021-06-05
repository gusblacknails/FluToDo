# How to run FluToDo

# Activate virtualevn
```source venv/bin/activate```

# Boot Docker
```docker-compose up```

# Migrate models
```docker-compose exec web python manage.py makemigrations```

```docker-compose exec web python manage.py migrate```



