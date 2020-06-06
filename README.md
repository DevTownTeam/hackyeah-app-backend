# hackyeah-app-backend

### Installation

Linux:
```
python3 -m venv venv
source venv/bin/activate
```

Windows:
```
python -m venv venv
venv\Scripts\activate
```

And then, for both systems:
```
pip install -r requirements.txt
cd backend
python3 manage.py migrate
python3 manage.py runserver
```

If you get an error while installing requirements, it's very likely that it is caused
by [psycopg2](https://stackoverflow.com/questions/5420789/how-to-install-psycopg2-with-pip-on-python).