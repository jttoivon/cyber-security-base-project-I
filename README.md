The notes app can be used to record notes that can be categorised
by adding one or more tags to each note. Multiple users are supported.
The notes app is implemented using the Django framework for creating a web application.

To start using the notes app, first issue the following command
to create necessary databases:
```python manage.py makemigrations notes``` and 
```python manage.py migrate```
Then create a superuser account with command
```python manage.py createsuperuser --username admin```
Finally start the server with 
```python manage.py runserver```

Then you can add normal users through the admin app by
opening the address `http://127.0.0.1:8000/admin` in your web browser.
After a normal user account has been created, access the notes app
from the following address:
http://127.0.0.1:8000/



