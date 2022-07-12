

# LendTech Challenge


## Setup


The first thing to do is to clone the repository:
```sh
$ git clone https://github.com/dave-cmd/Lendtech.git into a directory


$ cd into the directoty
```

Create a virtual environment to install dependencies in and activate it: 


In linux, run [python3 -m venv venv]

```sh
$ python3 -m venv venv

$ source venv/bin/activate
```

Then install the dependencies:
```sh
(venv)$ pip install -r requirements.txt
```

Once pip has finished downloading the dependencies:

```sh
(venv)$ cd project
(venv)$ python manage.py runserver
```

And navigate to http://127.0.0.1:8000/



## Walkthrough

Run the following commands to create a sqlite database in the working directory

```sh
(venv) $ python3 manage.py createsuperuser  
(venv) $ python3 manage.py makemigrations
(venv) $ python3 manage.py migrate
```

Access the admin panel with the credentilas created with the [createsuperuser ] command 
http://127.0.0.1:8000/admin


