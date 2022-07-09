

LendTech application


Setup


The first thing to do is to clone the repository:

$ git clone https://github.com/dave-cmd/Lendtech.git into a directory


$ cd into the directoty


Create a virtual environment to install dependencies in and activate it: 


In linux, run [python3 -m venv venv]

$ python3 -m venv venv

$ source venv/bin/activate

Then install the dependencies:

(venv)$ pip install -r requirements.txt


Once pip has finished downloading the dependencies:

(env)$ cd project
(env)$ python manage.py runserver
And navigate to http://127.0.0.1:8000/



Walkthrough
http://127.0.0.1:8000/admin can is accessible through [username: 'kanjuru'] && [password: 'root']

