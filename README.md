## TECHNICAL TEST API REST PYTHON

It's a simple REST API with Python 3.9

### Technologies

- [Python 3.9](https://www.python.org/downloads/)
- [mysql-connector-python](https://dev.mysql.com/downloads/connector/python/) allow connecting with the db in MYSQL
- [django-environ](https://pypi.org/project/django-environ-2/) allow to use environment variables in the project

### How I develop this project

I adopted the methodology of [Django](https://www.djangoproject.com/) with twelve-factor-app methodology

First I created the structure of the application with the following structure:

- .envs store all the environment variables
- .gitignore store the files that I don't want to be committed
- DB allows connecting with the database
- manage.py is the main file of the project
- requirements.txt is the list of the packages that I need to install
- settings are the configuration for the project
- urls.py is the configuration of the URL
- views.py is the configuration of the views
- server is the configuration of the server

## Questions before creating this project
### What is the purpose of this project?
This project is a technical test to verify my knowledge in backend development with Python.
I created an API rest that allows the users to see the properties available in habi.co and allow them to give a like the favorites properties.
### How I can create an API without the use of frameworks?
Well, it's my first time creating an API without the use of any frameworks, but I know if the project is with Python, I can create anything.

### How to use

```bash
  python3 -m venv .env
  source .env/bin/activate
  pip install -r requirements.txt
```
Now in the folder .envs/.production add the credentials for the database.
```bash
    MYSQL_HOST=<your database host>
    MYSQL_PORT=<your database port>
    MYSQL_USER=<your database username>
    MYSQL_PASSWORD=<your database password>>
    MYSQL_DATABASE=<your database name>
```


```bash
  python3 manage.py
```

Thank you HABI for the great experience.
