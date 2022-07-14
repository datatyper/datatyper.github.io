title: Creating a Flask App  
subtitle: Blogging the Easy Way
progress: 20%
author: Philip Mannering  
date: 2021-11-22  
category: python
tags: [flask, python]  

# Flask - Creating and Deploying a Web App

This is a short guide to creating and deploying an app using the [Flask](http://flask.pocoo.org/) framework to create a web app. The app is deployed to the [Heroku](https://www.heroku.com/) platform. And the console used is PowerShell.

## Part 1: Setting up the Project Locally

These first few steps provide the minimum required to setup the project locally.

1. Create a virtual environment
    ```
    mkdir <project_name>
    cd <project_name>
    python -m venv env
    ```
    This creates a separate python environment `env` for the project. It prevents the dependencies of other projects from conflicting with one another.

1. Activate the virtual environment
    ```
    .\venv\Scripts\activate
    ```
    Activate the environment to start using and installing packages for the newly created project.

1. Install Flask and other packages you may require later
    ```
    pip install flask
    pip install flask-flatpages
    pip install gunicorn
    ```
    Install the Flask package and any other modules you need. 
    **Flask** is the web framework that handles our requests
    **Flask-FlatPages** allows us to build web pages from markdown text files  
    **Gunicorn** is a WSGI server used to run the app on Heroku.

1. Create the app
    Inside `app.py` write your app. A minimal version might look something like this:
    ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'Hello World!'

    if __name__ == '__main__':
        app.run(debug=True)
    ```
    This code creates a Flask app called _app_ and defines a route for the `/` endpoint to return the string "Hello World!".

    You can test the app locally by typing `python app.py` into the terminal. You should see the string "Hello World!" in the browser by going to [localhost:5000](http://localhost:5000/)

Congratulations! You've taken the first steps to creating a live app.

---




### 4. Create a requirements.txt file
Create a `requirements.txt` file with the packages you need to install.
```
pip freeze > requirements.txt
```

### 6. Initialize a git repository
```
git init
```
Initialize a git repository to track changes to the app and ultimately push to the Heroku platform.


### 7. Create a .gitignore file and add the following lines
```
venv
__pycache__
```
Everything added to the `.gitignore` file will be ignored by git. We aren't interested in tracking the virtual environment and the python cache.

### 8. Add and commit changes to git
```
git add .
```
9. Commit the changes
```
git commit -m "Initial commit"
```
10. Log into Heroku
```
heroku login
```


