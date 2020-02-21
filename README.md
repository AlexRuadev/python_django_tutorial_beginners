##### https://docs.djangoproject.com/en/3.0/intro/tutorial01/

## Create virtual environmennt
  python -m venv env
  cd env/Scripts
  source activate

## Install Django
  pip install django

## Start project
  A la racine du projet : 
    django-admin startproject mysite
    cd mysite/

## we can now login to dashboard
  python manage.py runserver

## to configure database, use migrate command (in your project)
  python manage.py migrate

## create a superuser/admin (fac)
  python manage.py createsuperuser
  # Then run you server
  python manage.py runserver


### exemple, get polls app from django documentation
  ## go to the same level as manage.py  (check with ls that manage.py is listed)
    python manage.py startapp polls

## after you created your models for polls app, and you have added polls to your installed apps in your project(mysite), run:
  python manage.py makemigrations polls

## after you have made those migration, you want to commit them to your database
  python manage.py migrate
