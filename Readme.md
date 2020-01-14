# dg_gql_recipes
Example of django - GraphQL CI/CD project.

[![Build Status](https://travis-ci.org/NajlaBH/dg_gql_recipes.svg?branch=master)](https://travis-ci.org/NajlaBH/dg_gql_recipes)
[![CircleCI](https://circleci.com/gh/NajlaBH/dg_gql_recipes.svg?style=svg)](https://circleci.com/gh/NajlaBH/dg_gql_recipes)
[![DJANGO:version](https://img.shields.io/badge/Django-2.2.9-blue.svg)](https://www.djangoproject.com/download)

### Getting Started
https://github.com/NajlaBH/gql-dg-tmp.git


### HowTo

1. Clone the repository :

  ```bash
git clone https://github.com/NajlaBH/dg_gql_recipes.git
cd dg_gql_recipes
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
 ```

2. Make migrations :
 
  ```bash
python manage.py makemigrations
python manage.py migrate
 ```
 
3. Create superuser (To get admin interface):
 
  ```bash
python manage.py createsuperuser
 ```
 
4. Load json data :
 
  ```bash
 python ./manage.py loaddata recipes_data.json
 ```  
   
5. Run the server :
 
  ```bash
python manage.py runserver 0.0.0.0:8080
 ```

6. Examples :
	- You can try same queries examples from :
 https://github.com/NajlaBH/dg_gql_recipes/blob/master/tests/queries_test.txt
	- You can try some mutations examples from : 
 https://github.com/NajlaBH/dg_gql_recipes/blob/master/tests/mutations_test.txt

### Authors 
NajlaBH

### Related projects
* https://realpython.com/get-started-with-django-1/
* https://github.com/Fueled/django-init
* https://circleci.com/docs/2.0/language-python/
* https://circleci.com/docs/2.0/workflows/
* https://graphene-python.org/
* https://docs.graphene-python.org/projects/django/en/latest/tutorial-plain/

### LICENSE
MIT
