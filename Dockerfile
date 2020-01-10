FROM python:3.8.1
LABEL "AUTHOR NAJLABH JAN_2020"
ENV PYTHONUNBUFFERED 1
RUN mkdir /NajlaBH/recipesApp
WORKDIR /NajlaBH/recipesApp
ADD requirements.txt /NajlaBH/recipesApp/
RUN pip install -r requirements.txt
ADD . /NajlaBH/recipesApp/
CMD sh init.sh && python3 manage.py runserver 0.0.0.0:8000
