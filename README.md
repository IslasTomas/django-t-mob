install mysql

- sudo apt update
- sudo apt install mysql-server

create database and user with permissions

- sudo mysql
- CREATE DATABASE database_name
- CREATE USER 'username' IDENTIFIED BY 'password'
- GRANT ALL PRIVILEGES ON database_name.\* TO username

install memcached

- sudo apt-get install memcached
- pip install pymemcache
  install enviroment

- virtualenv --python=python3 environment_name
- source environment_name/bin/source activate
- pip install -r requirements.txt

config .env

- copy and paste examen/ .env.example and define variables
  run migrations

- python manage.py migrate

loaddata

- python manage.py loaddata data.json

create super user

-python manage.py createsuperuser

run server

-python manage.py runserver
