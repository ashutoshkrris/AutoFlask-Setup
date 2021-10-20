# AutoFlask-Setup

### About
AutoFlask-Setup can help you set up a new Flask Project, right from creating virtual environment to creating Procfile for deployment.


### Requirements

* Python (3.6+)

### Usage

* Just copy the `setup.py` file in your directory, wherever you want your project to be setup.
* Important Commands:
    * `python setup.py` - About AutoFlask-Setup
    * `python setup.py help` - Get Necessary Commands List
    * `python setup.py copyright` - Get Copyright Information
    * `python setup.py credits` - Get Credits Information
    * `python setup.py license` - Get License Information
    * `python setup.py initproject` - Initialize Flask Project

* Once the project setup is complete, you can delete the `setup.py` file safely.


### Example

```bash
$ py setup.py 

AutoFlask-Setup can help you set up a new Flask Project, right from creating virtual environment to creating Procfile for deployment.
AutoFlask-Setup(v1.0.0, Oct 20 2021, 8:25:39)
Add arguments like "help", "copyright", "credits" or "license" for more information.

DEVIL@ASHUTOSH-PC MINGW64 /d/Quarantine/Flask/Test (main)
$ py setup.py initproject

Initiating Project Setup

Creating and activating a virtual environment...
Installing virtualenv on Windows ... 

[+] virtualenv installed.

Creating A New virtualenv ...
Virtual environment activated successfully

Installing required dependencies...
Collecting Flask
  Using cached Flask-2.0.2-py3-none-any.whl (95 kB)
Collecting Flask-Migrate
  Using cached Flask_Migrate-3.1.0-py3-none-any.whl (20 kB)
Collecting Flask-SQLAlchemy
  Using cached Flask_SQLAlchemy-2.5.1-py2.py3-none-any.whl (17 kB)
Collecting Flask-Mail
  Using cached Flask_Mail-0.9.1-py3-none-any.whl
Collecting python-decouple
  Using cached python_decouple-3.5-py3-none-any.whl (9.6 kB)
Collecting itsdangerous>=2.0
  Using cached itsdangerous-2.0.1-py3-none-any.whl (18 kB)
Collecting Werkzeug>=2.0
  Using cached Werkzeug-2.0.2-py3-none-any.whl (288 kB)
Collecting click>=7.1.2
  Using cached click-8.0.3-py3-none-any.whl (97 kB)
Collecting Jinja2>=3.0
  Using cached Jinja2-3.0.2-py3-none-any.whl (133 kB)
Collecting alembic>=0.7
  Using cached alembic-1.7.4-py3-none-any.whl (209 kB)
Collecting SQLAlchemy>=0.8.0
  Using cached SQLAlchemy-1.4.26-cp39-cp39-win_amd64.whl (1.5 MB)
Collecting blinker
  Using cached blinker-1.4-py3-none-any.whl
Collecting Mako
  Using cached Mako-1.1.5-py2.py3-none-any.whl (75 kB)
Collecting colorama
  Using cached colorama-0.4.4-py2.py3-none-any.whl (16 kB)
Collecting MarkupSafe>=2.0
  Using cached MarkupSafe-2.0.1-cp39-cp39-win_amd64.whl (14 kB)
Collecting greenlet!=0.4.17
  Using cached greenlet-1.1.2-cp39-cp39-win_amd64.whl (101 kB)
Installing collected packages: MarkupSafe, colorama, Werkzeug, Jinja2, itsdangerous, greenlet, click, SQLAlchemy, Mako, Flask, Flask-SQLAlchemy, blinker, alembic, python-decouple, Flask-Migrate, Flask-Mail
Successfully installed Flask-2.0.2 Flask-Mail-0.9.1 Flask-Migrate-3.1.0 Flask-SQLAlchemy-2.5.1 Jinja2-3.0.2 Mako-1.1.5 MarkupSafe-2.0.1 SQLAlchemy-1.4.26 Werkzeug-2.0.2 alembic-1.7.4 blinker-1.4 click-8.0.3 colorama-0.4.4 greenlet-1.1.2 itsdangerous-2.0.1 python-decouple-3.5
All dependencies installed successfully

Creating package
Package created successfully

Creating app runner...
App runner created successfully

Creating configurations file...
Configurations file created successfully

Creating templates and static directory...
Templates and static directory created successfully

Creating routes...
Routes created successfully

Creating models...
Models created successfully

Creating miscellaneous files...
 * Tip: There are .env or .flaskenv files present. Do "pip install python-dotenv" to use them.
Creating directory D:\Quarantine\Flask\Test\migrations ...  done
Creating directory D:\Quarantine\Flask\Test\migrations\versions ...  done
Generating D:\Quarantine\Flask\Test\migrations\alembic.ini ...  done
Generating D:\Quarantine\Flask\Test\migrations\env.py ...  done
Generating D:\Quarantine\Flask\Test\migrations\README ...  done
Generating D:\Quarantine\Flask\Test\migrations\script.py.mako ...  done
Please edit configuration/connection/logging settings in 'D:\\Quarantine\\Flask\\Test\\migrations\\alembic.ini' before proceeding.
Miscellaneous files created successfully

Project Setup Complete

Please make necessary changes in '.env' file.
Please run 'python setup.py help' for necessary commands.
```