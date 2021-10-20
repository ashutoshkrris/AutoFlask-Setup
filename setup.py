import os
import sys
import pathlib
import platform
import subprocess


MAIN_FILE_CONTENT = """\
from app import app

if __name__ == "__main__":
    app.run()
"""

CONFIG_FILE_CONTENT = """\
from decouple import config

DATABASE_URI = config("DATABASE_URL")
if DATABASE_URI.startswith("postgres://"):
    DATABASE_URI = DATABASE_URI.replace("postgres://", "postgresql://", 1)


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config("EMAIL_ADDRESS")
    MAIL_PASSWORD = config("EMAIL_PASSWORD")
    MAIL_DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    MAIL_DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
"""

ENV_FILE_CONTENT = """\
APP_SETTINGS=config.DevelopmentConfig
SECRET_KEY=TFP5U-4QJFayXuAG83-^vhcPCwf??jt5Z@CU9zXxy&5@F2A!n3y%hVmVAnMNBSLh$Tj9YZb73e7sBh6KeXCGRDSc9z&fBt4v
DATABASE_URL=sqlite:///app.db
EMAIL_ADDRESS=youremail@gmail.com
EMAIL_PASSWORD=verystrongpassword
"""

GITIGNORE_FILE_CONTENT = """\
.DS_Store
.env
.flaskenv
*.pyc
*.pyo
env/
venv/
.venv/
env
dist/
build/
*.egg
*.egg-info/
_mailinglist
.tox/
.cache/
.pytest_cache/
.idea/
docs/_build/
.vscode

# Coverage reports
htmlcov/
.coverage
.coverage.*
*,cover
"""

PROCFILE_CONTENT = """\
web: gunicorn main:app
"""

INIT_FILE_CONTENT = """\
from decouple import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

db = SQLAlchemy(app)
if db.engine.url.drivername == 'sqlite':
    migrate = Migrate(app, db, render_as_batch=True)
else:
    migrate = Migrate(app, db)
mail = Mail(app)

from app import routes, models
"""

ROUTES_FILE_CONTENT = """\
from app import app, db, mail
from flask import render_template, redirect, jsonify
from flask_mail import Mail, Message


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
"""

MODELS_FILE_CONTENT = """\
from app import db
"""


def help_menu():
    necessary_commands = [
        ['Commands', 'Description'],
        ['',''],
        ['python setup.py initproject', 'To setup a new flask project'],
        ['flask db init', 'To initialize flask migrations repository'],
        ['flask db migrate', 'To migrate new changes in the table'],
        ['flask db migrate -m <message>', 'To migrate new changes in the table with specific message'],
        ['flask db upgrade', 'To upgrade database with the latest migrations'],
        ['flask db downgrade', 'To downgrade database with the previous migrations'],
        ['git init', 'To initialize new Git repository'],
        ['git add .', 'To add all files to the Git repository'],
        ['git add <filename>', 'To add specific file to the Git repository'],
        ['git remote add origin <origin-url>', 'To add origin to the Git repository'],
        ['git commit -m <message>', 'To commit files with a message'],
        ['git push origin <branch-name>', 'To push files in the given branch of the origin'],
        ['git pull origin <branch-name>', 'To pull files from the given branch of the origin'],
        ['git checkout -b <branch-name>', 'To create a new branch'],
        ['git checkout <branch-name>', 'To move to any branch'],
    ]

    for command in necessary_commands:
        print("{: >40}        {: >40}".format(*command))
    

def copyright():
    print("\nCopyright (c) 2021 Ashutosh Krishna\n All Rights Reserved.")


def credits():
    print("\nThanks to Pallets Projects for the continuously developing Flask. See www.flask.palletsprojects.com/en/2.0.x/ for more information.\nThanks to Python Software Foundation for continuously developing Python. See www.python.org for more information.")


def license():
    print("""
    AutoFlask-Setup is licensed under the MIT License.
    
    MIT License

    Copyright(c) 2021 Ashutosh Krishna

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files(the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and / or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.""")


# This function will install virtualenv, then create a new venv, and activate it
def install_venv(os_version):
    print(f"Installing virtualenv on {os_version} ... ")
    if os_version == "Windows":
        os.system("python -m pip install virtualenv >nul 2>&1")
        print("\n[+] virtualenv installed.")
        print("\nCreating A New virtualenv ... ")
        os.system("python -m virtualenv env >nul 2>&1")

    else:
        subprocess.run("pip install virtualenv",
                       shell=True, stdout=subprocess.PIPE)
        print("\n[+] virtualenv installed.")
        print("\nCreating A New virtualenv ... ")
        subprocess.run("virtualenv env", shell=True,
                       stdout=subprocess.PIPE)


def initialize_project():
    print("\nInitiating Project Setup")
    package_name = "app"
    base_dir = pathlib.Path(__file__).resolve().parent

    # Create a virtual environment and activate it
    print("\nCreating and activating a virtual environment...")
    install_venv(platform.system())
    print("Virtual environment activated successfully")

    # Install dependencies
    print("\nInstalling required dependencies...")
    pip_path = os.path.join(base_dir, "env", "Scripts", "pip")
    os.system(
        f"{pip_path} install Flask Flask-Migrate Flask-SQLAlchemy Flask-Mail python-decouple")
    os.system(f'{pip_path} freeze > requirements.txt')
    print("All dependencies installed successfully")

    # Create package
    print("\nCreating package")
    os.system(f"mkdir {package_name}")
    # os.system(f'touch {package_name}/__init__.py')
    with open(os.path.join(base_dir, f"{package_name}/__init__.py"), "w") as f:
        f.write(INIT_FILE_CONTENT)
    print("Package created successfully")

    print("\nCreating app runner...")
    # os.system('touch main.py')
    with open(os.path.join(base_dir, "main.py"), "w") as f:
        f.write(MAIN_FILE_CONTENT)
    print("App runner created successfully")

    print("\nCreating configurations file...")
    with open(os.path.join(base_dir, "config.py"), "w") as f:
        f.write(CONFIG_FILE_CONTENT)
    print("Configurations file created successfully")

    print("\nCreating templates and static directory...")
    os.chdir(package_name)
    os.system(f'mkdir static')
    os.system(f'mkdir templates')
    os.chdir(base_dir)
    print("Templates and static directory created successfully")

    print("\nCreating routes...")
    with open(os.path.join(base_dir, f"{package_name}/routes.py"), "w") as f:
        f.write(ROUTES_FILE_CONTENT)
    print("Routes created successfully")

    print("\nCreating models...")
    with open(os.path.join(base_dir, f"{package_name}/models.py"), "w") as f:
        f.write(MODELS_FILE_CONTENT)
    print("Models created successfully")

    print("\nCreating miscellaneous files...")
    with open(os.path.join(base_dir, ".env"), "w") as f:
        f.write(ENV_FILE_CONTENT)
    with open(os.path.join(base_dir, "Procfile"), "w") as f:
        f.write(PROCFILE_CONTENT)
    with open(os.path.join(base_dir, ".gitignore"), "w") as f:
        f.write(GITIGNORE_FILE_CONTENT)
    os.system('flask db init')
    print("Miscellaneous files created successfully")

    print("\nProject Setup Complete")
    print("\nPlease make necessary changes in '.env' file.")
    print("Please run 'python setup.py help' for necessary commands.")



if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg == "help":
            help_menu()
        elif arg == "copyright":
            copyright()
        elif arg == "credits":
            credits()
        elif arg == "license":
            license()
        elif arg == "initproject":
            initialize_project()
    else:
        print('\nAutoFlask-Setup can help you set up a new Flask Project, right from creating virtual environment to creating Procfile for deployment.\nAutoFlask-Setup(v1.0.0, Oct 20 2021, 8:25:39)\nAdd arguments like "help", "copyright", "credits" or "license" for more information.')
