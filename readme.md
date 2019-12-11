# Job parser applications

My first ever working app, this monument will stay here forever. It pars specific jobs in specific locations (depend on user input) on indeed website and show specific feathers of jobs posting (position, company, salary and url).

Now working on refactoring the code according to industry standards. Need to implement:
- django forms for collecting input from user
- django forms validators for clear input data
- python url constructor for construct urls less manually

---

# Django applications

# How to develope\deploy application
## Back-end
- Add app to your INSTALLED_APPS - project/settings.py
- Create models - app/models.py
- Migrate - python manage.py migrate
- Add Views - app/views.py
- Add forms if needed - app/forms.py
## Routing
- Add app URLS - app/urls.py
- Add project URLS - project/urls.py
## Front-end
- Add Templates - app/templates/something.html
- Add static files - app/static
## Administration
- Add superuser if needed - python manage.py createsuperuser
- Add class to admin interface - app/admin.py

## Django basics

### Install virtual environment:
```
python - m pip install virtualenvwrapper-win
```

### Create a virtual environment for your project
```
mkvirtualenv myproject
```

### Activate virtual environment:
```
workon myproject
```
- django_apps for that specific app

### Create project:
```
django-admin startproject project_name
```

### Create application:
```
python manage.py startapp app_name
```

### Run virtual server:
```
python manage.py runserver
```

### Create superuser
```
python manage.py createsuperuser
```

### Create a migration file
```
python manage.py makemigrations projects
```
### Apply the migrations set out in the migrations file and create your database
```
python manage.py migrate projects
```
### Get access to Django shell
```
python manage.py shell
```

---
# Django on heroku

### Procfile file
**Important** to name your project, not an app!
```
web: gunicorn project_name.wsgi
```
### runtime.txt
Version of the python
```
python-3.6.8
```

### requirements.txt
Requirements files are used to hold the result from pip freeze for the purpose of achieving repeatable installations. In this case, your requirement file contains a pinned version of everything that was installed when pip freeze was run.
```
pip install -r requirements.txt
pip freeze > requirements.txt
```

### ALLOWED_HOSTS
add host of your app on heroku to: your_project/settings.py

```python
ALLOWED_HOSTS = ['your_heroku_app.herokuapp.com']
```
