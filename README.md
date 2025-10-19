** Django Events & Booking API**


A Django REST Framework–based backend for managing users, events, and bookings.
It supports authentication with JWT tokens, and provides clean, RESTful API endpoints for managing event creation, ticket bookings, and user profiles.

** 🚀 Features ** 

User registration, authentication (JWT)

Event creation, update, delete, and listing

Booking management (create, view, cancel)

Pagination, filtering, and search on events

Admin dashboard for managing all data

Modular app structure (users, events, bookings)

Fixtures for quick sample data loading

🛠️ Tech Stack

Python 3.12+

Django 5.2

Django REST Framework (DRF)

PostgreSQL (or SQLite for local testing)

JWT Authentication via djangorestframework-simplejwt

django-filter for filtering and searching

⚙️ Setup & Installation
1. Clone the Repository
git clone https://github.com/yourusername/django-events-booking.git
cd django-events-booking

2. Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate    # on Windows
source venv/bin/activate # on macOS/Linux

3. Install Dependencies
pip install -r requirements.txt

4. Database Setup

In events_booking/settings.py, configure your database:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'eventprojectdb',
        'USER': 'ethio',
        'PASSWORD': 'ethio_12',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


Then apply migrations:

python manage.py migrate

5. Load Sample Fixtures (optional)
python manage.py loaddata users.json
python manage.py loaddata events.json
python manage.py loaddata bookings.json

6. Create a Superuser
python manage.py createsuperuser

7. Run the Server
python manage.py runserver


Admin Panel → http://127.0.0.1:8000/admin/

API Root → http://127.0.0.1:8000/api/

🔐 Authentication (JWT)
Obtain Tokens
POST /api/token/
Content-Type: application/json

{
  "username": "your_username",
  "password": "your_password"
}

Response:
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}


Use the token in your requests:

Authorization: Bearer <your_access_token>

Refresh Token
POST /api/token/refresh/
{
  "refresh": "your_refresh_token"
}

📦 API Endpoints
Resource	Endpoint	Methods	Description
Users	/api/users/	GET, POST, PUT, DELETE	Manage users
Events	/api/events/	GET, POST, PUT, DELETE	Manage events
Bookings	/api/bookings/	GET, POST, PUT, DELETE	Manage bookings
JWT Token	/api/token/	POST	Obtain access/refresh tokens
Token Refresh	/api/token/refresh/	POST	Refresh access token
📬 Postman Collection Setup

You can use Postman to test all API endpoints easily.

1. Get Token

Method: POST

URL: http://127.0.0.1:8000/api/token/

Body (raw JSON):

{
  "username": "admin",
  "password": "yourpassword"
}


Response: Copy access token.

2. Add Authorization Header

Go to Authorization → Type: Bearer Token

Paste your token:

Authorization: Bearer <your_access_token>

3. Create an Event

Endpoint: POST http://127.0.0.1:8000/api/events/
Body (JSON):

{
  "title": "Tech Conference 2025",
  "description": "Annual technology conference",
  "location": "Addis Ababa",
  "start_time": "2025-12-01T09:00:00Z",
  "end_time": "2025-12-01T18:00:00Z",
  "capacity": 200,
  "price": "100.00"
}

4. Book an Event

Endpoint: POST http://127.0.0.1:8000/api/bookings/
Body (JSON):

5. Get Events / Bookings
GET http://127.0.0.1:8000/api/events/
GET http://127.0.0.1:8000/api/bookings/

