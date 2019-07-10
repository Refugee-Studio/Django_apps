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
python - m pip install virtualenvwrapper-win

### Create a virtual environment for your project
mkvirtualenv myproject

### Activate virtual environment:
workon myproject

### Create project:
django-admin startproject project_name

### Create application:
python manage.py startapp app_name

### Run virtual server:
python manage.py runserver

### Create superuser
python manage.py createsuperuser

### Create a migration file
python manage.py makemigrations projects
### Apply the migrations set out in the migrations file and create your database
python manage.py migrate projects

### Get access to Django shell
python manage.py shell

