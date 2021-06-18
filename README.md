[![CircleCI](https://circleci.com/gh/Arrotech/flask-api.svg?style=svg)](https://circleci.com/gh/Arrotech/flask-api) [![Build Status](https://dev.azure.com/arrotech254/Azure%20Pipeline/_apis/build/status/Arrotech.flask-api?branchName=develop)](https://dev.azure.com/arrotech254/Azure%20Pipeline/_build/latest?definitionId=1&branchName=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/16fcf66b72437e32b882/maintainability)](https://codeclimate.com/github/Arrotech/flask-api/maintainability)

# Flask MVC/API (Starter Template)

You will learn how to use the following `flask MVC/API template` to create a `large` and `modularized applications`.

# Getting Started

1. Clone the following [repo](https://github.com/Arrotech/flask-api.git) to your local machine.
2. Create a local virtual environment inside the root directory of the cloned [repo](https://github.com/Arrotech/flask-api.git) i.e `python3 -m venv venv` in linux or `python -m venv venv` in windows.
3. To activate the environment first navigate to the `.env` file and comment or uncomment the environment activation line according to your operating system then simply activate the environment by typing: `source .env`. Alternatively you can activate the environment by typing the whole path: In windows `source venv/Scripts/activate` or `source venv/bin/activate` in linux.
4. Install all the required dependencies as follows: `pip install -r requirements.txt`.
5. If you want to use your own database, navigate to the root directory and find `.env` file and update the `DATABASE_URI` and `TEST_DATABASE_URI`.


**NB** You should also update your `APP SECRET KEY` from the `.env` file.

# How to run the application.

To run the application run the following command `flask run`.

**NB** Make sure your virtual environment is activated.

# Growing Your Application

## 1. Models

### i. Get your database working

1. First you should `create a database` where you will store your data.
2. Next you will need to `update` your `database configurations` on the `.env` file by providing details specific to your database.

        export DATABASE_URI='YOUR_DB_URI'
        export TEST_DATABASE_URI='YOUR_TEST_DB_URI'

### ii. Performing Migrations

Performing migrations is as simple as:
1. Initialize migration by running: `python3 manage.py db init`
2. Then migrate your db by running: `python3 manage.py db migrate`
3. Finally you need to apply migrations by running: `python3 manage.py db upgrade`
**NB**1. If tables do not exist they will be created after applying migrations.
**NB**2. In case you update your models all you need to do is to create a new migration and apply the migration. This will only involve `step 1` and `step 2`.

### iii. Create New Models

To learn how to create models please follow the standards of [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/).

A simple model would be:

```
from app.extensions import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
```

All you need to do is to import `db` instance from `extensions` file.

### iv. Adding New Files

You can also add your own model files by just creating a new file within the models folder.

**Example**

1. A good example would be creating a file by the name `users_models.p` the you can add your own models with in that file.
2. Finally import the file to you `app/__init__.py` file as follows.

Update `app/__init__.py` file.

```
def create_app(config_name):

    ...

    from app.api.v1.home import models
    from app.api.v1.home import users_model # new line

    db.init_app(app)

    ...
```

**Testing Your Models**

In order to test your models navigate to `tests/v1/base_test.py` and uncomment the following lines
1. db import `# from app.extensions import db`
2. create db `# db.create_all()`
3. destroy db `# db.drop_all()` 

## 2. Views

## 3. Services

## 4. Configurations

## 5. Utilities 

## 6. Tests

## 7. Virtual Environment and Environment Variables

**DISCLAIMER (:**
DO NOT push your `.env` files to any version control service such as `GITHUB`. In this tutorial I only did it so you can have an idea of how to use one. This file is for storing secure and private information about you application such as `passwords`, `secret_key`, e.t.c.
A good practice is to add your `.env` file to a `.gitignore` file. This will prevent future push therofore protecting you private data.

## 8. Version Control

## 9. Continuous Integration

## 10. Deployment

# Author

    Harun Gachanja Gitundu.
