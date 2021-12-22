# Una Health Project
## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/brianmafu/unahealth_project.git
$ cd unahealth_project
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv .env
$ source .env/bin/activate
```

Then install the dependencies:

```sh
(.env)$ pip install -r requirements.txt

(.env)$ cd unahealth_project
(.env)$ python manange.py migrate
(.env)$ python manange.py createsuperuser


(.env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`. for Frontend
And navigate to `http://127.0.0.1:8000/api/v1/`. for API


