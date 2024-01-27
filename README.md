Requirements 
Django 4.1.0 or above (previous versions should support Django all the way back to around 3.1).

Installation
Step 1 
Get the code: python -m venv venv

Step 2
Get the code: pip install requirements.txt

Step 2
Get the code: python manage.py runserver 


You are good to go

-------------------------------------------------------------------------------------------------
1. Install IPython:
First, make sure you have IPython installed in your virtual environment. You can install it using:

pip install ipython


2. Configure Django Settings:
Open your Django project's settings.py file and add the following line at the end of the file:

SHELL_PLUS = "ipython"


3. Install django-extensions:
You might need to install the django-extensions package, which provides the shell_plus management command:

pip install django-extensions


And You will have beauiful shell in django
-------------------------------------------------------------------------------------------------