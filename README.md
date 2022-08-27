# DVD_RentalApp
Example using Dockerf, Django and SQL DataBase

## Instructions
1. Create virtual environment `python3 -m venv myenv`
2. Activate it `source myenv/bin/activate`
3. `python -m pip install -r requirements.txt`
4. `cd DVD_RentalApp/`
5. `python manage.py runserver`

## ENDPOINTS

## To register a new user

Go to the page and complete the form:
```
http://127.0.0.1:8000/api/v1/auth/register/
```
or send with postman the following information, as the example:
```
http POST http://127.0.0.1:8000/api/v1/auth/register/ email="email@email.com" username="myuser" password="noCommonPass123" password2="noCommonPass123"
```
- Note: The information is in auth_user table

## Get new token pair

Go to the page and complete the form:
```
http://127.0.0.1:8000/api/v1/auth/token/
```
or send with postman the following information, as the example:
```
http POST http://127.0.0.1:8000/api/v1/auth/token/ username="myuser" password="noCommonPass123"
```

## Refresh the access token
Send your old refresh token to obtain your new access token.
Go to page and paste the token: 
```
http://127.0.0.1:8000/api/v1/auth/refresh/
```
or send with postman the following information, as the example:
```
http POST http://127.0.0.1:8000/api/v1/auth/token/refresh/ refresh="
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MTcwNDI2MCwianRpIjoiOTYxMTg0YjVkMzZhNDZkZjg2ZjcxZDdkNWI2ODBjNWQiLCJ1c2VyX2lkIjozfQ.-70g8mc2rcZa0jDtLmhhEFaoWIcfc6F1JlbekHLHzuM"
```

## Commands
Get all movies
```
http http://127.0.0.1:8000/api/v1/movies/ "Authorization: Bearer {eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxNjE5MTUxLCJqdGkiOiJjNGU3MzViYjUzYTA0ZTBjYjAyOTM1OGY2ZmNkMDQ1ZCIsInVzZXJfaWQiOjJ9.l5Se847FJcXumUFQGoONL6hT40sZ06nNsGo6uTnx_6Y}" 
```

Get a single movie
```
http GET http://127.0.0.1:8000/api/v1/movies/{movie_id}/ "Authorization: Bearer {YOUR_TOKEN}" 
```

Create a new movie
```
http POST http://127.0.0.1:8000/api/v1/movies/ "Authorization: Bearer {YOUR_TOKEN}" title="The Shining" release_year=2018 number_in_stocks=5 daily_rate=2.2 genre=2
```

Full update a movie
```
http PUT http://127.0.0.1:8000/api/v1/movies/{movie_id}/ "Authorization: Bearer {YOUR_TOKEN}" title="The Shining" release_year=2018 number_in_stocks=5 daily_rate=2.2 genre=2
```

Partial update a movie
```
http PATCH http://127.0.0.1:8000/api/v1/movies/{movie_id}/ "Authorization: Bearer {YOUR_TOKEN}" title="The Shining2" 
```

Delete a movie
```
http DELETE http://127.0.0.1:8000/api/v1/movies/{movie_id}/ "Authorization: Bearer {YOUR_TOKEN}"
```