# How run FluToDo

# up virtualevn
```source venv/bin/activate```

# Run Docker
```docker-compose up```

# Migrate models
```docker-compose exec web python manage.py makemigrations```

```docker-compose exec web python manage.py migrate```

