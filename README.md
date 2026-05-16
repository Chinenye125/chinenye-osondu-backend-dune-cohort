# ToriloShop - Django Project

# Backend Dune Cohort

## Django Modules Progress

This repository contains all Django assignment solutions for the Dune Cohort.


## Module 8: Django Models, ORM, SQL & Migrations

- **Project:** ToriloShop (Extended with Category and Product models)
- **Key Features:** Django Models, ForeignKey relationship, ORM queries,
  Migrations, Django Admin
- **Submission Folder:** module-8/

### How to Run Module 8

- cd module-8/toriloshop
- ../../venv/Scripts/activate # Windows
- ../../venv/bin/activate # Mac/Linux
- python manage.py runserver


## Module 9: Django Templates & Static Files

- **Project:** ToriloShop (Extended with Templates and Static Files)
- **Key Features:** Django Templates, Bootstrap, DTL,
  Template Inheritance, Static Files
- **Submission Folder:** module-9/

### How to Run Module 9

cd module-9/toriloshop
../venv/Scripts/activate # Windows
python manage.py runserver


## Module 10: Django Forms, ModelForms & Full CRUD
- **Project:** ToriloShop (Extended with Full CRUD Operations)
- **Key Features:** ModelForms, Form Validation, CSRF Protection,
  Create, Read, Update, Delete for Products and Categories,
  Flash Messages, Search Feature
- **Submission Folder:** module-10/

### How to Run Module 10
- cd module-10
- ..\venv\Scripts\activate
- python manage.py runserver


## Module 11: Django Media Files, Admin Customization & UI Enhancements

- **Project:** Toriloshop (Extended with Media Handling and Admin Improvements)  
- **Key Features:** ImageField for Products, Media configuration (MEDIA_URL & MEDIA_ROOT), Custom CSS styling, Django Admin customization (list_display, search_fields, list_filter), custom admin actions (Mark as out of stock), collectstatic  
- **Submission Folder:** module-11/

### How to Run Module 11

- cd module-11  
- ..\venv\Scripts\activate  
- pip install pillow  
- python manage.py makemigrations  
- python manage.py migrate  
- python manage.py runserver  


## Module 12: Django Authentication & Permissions System

- **Project:** Toriloshop (Extended with User Authentication System)  
- **Key Features:** User Registration, Login, Logout, Protected Routes using @login_required, Staff-only delete permissions (is_staff check), Dynamic Navbar (Login/Register vs Username/Logout), Custom authentication forms and templates  
- **Submission Folder:** module-12/

### How to Run Module 12

- cd module-12  
- ..\venv\Scripts\activate  
- python manage.py makemigrations  
- python manage.py migrate  
- python manage.py createsuperuser  
- python manage.py runserver


## Module 13: Django REST Framework API Development

- **Project:** ToriloShop (Converted into a REST API)
- **Key Features:** Django REST Framework setup, Serializers (Product & Category),
  APIViews, CRUD API endpoints, nested category representation,
  Category product count using SerializerMethodField

- **API Endpoints:**
  - GET `/api/products/` → List all products
  - POST `/api/products/` → Create product
  - GET `/api/products/<id>/` → Retrieve single product
  - PUT `/api/products/<id>/` → Update product
  - DELETE `/api/products/<id>/` → Delete product
  - GET `/api/categories/` → List all categories with products

- **Submission Folder:** module-13/

### How to Run Module 13

- cd module-13
- ..\venv\Scripts\activate
- pip install djangorestframework
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver


## Module 14: Django REST Framework Security & API Enhancements

- **Project:** ToriloShop (Secured REST API System)
- **Key Features:** Token Authentication, JWT Authentication,
  Permission-based access control, created_by field (product ownership),
  IsAuthenticated protection, IsOwnerOrReadOnly custom permission,
  Pagination (6 products per page), Filtering, Search, Ordering,
  CORS configuration for frontend access

- **Security Features:**
  - Only authenticated users can create products
  - Only product owners can edit/delete products
  - Token Authentication + JWT Authentication support
  - Protected API endpoints

- **API Enhancements:**
  - Pagination with next/previous links
  - Filter by category and availability
  - Search by product name
  - Order by price

- **Submission Folder:** module-14/

### How to Run Module 14

- cd module-14
- ..\venv\Scripts\activate
- pip install djangorestframework djangorestframework-simplejwt django-cors-headers
- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver


## Module 15: Production Deployment Setup

- **Project:** ToriloShop (Production Ready Django REST API)
- **Key Features:** Environment variable configuration (.env),
  python-decouple integration, dj-database-url setup,
  Waitress WSGI server configuration, WhiteNoise for static files,
  collectstatic setup, Procfile creation, requirements.txt generation,
  Render deployment configuration

- **Production Tools Used:**
  - python-decouple (environment variables)
  - dj-database-url (database configuration)
  - Waitress (production server)
  - WhiteNoise (static file serving)
  - Render deployment setup

- **Deployment Features:**
  - Secure SECRET_KEY management
  - DEBUG configuration via environment variables
  - PostgreSQL support (production)
  - SQLite fallback (local development)
  - Static files handling in production

- **Submission Folder:** module-15/

### How to Run Module 15

- cd module-15
- ..\venv\Scripts\activate
- pip install gunicorn waitress python-decouple dj-database-url whitenoise psycopg2-binary
- python manage.py collectstatic
- waitress-serve --host=0.0.0.0 --port=8000 toriloshop.wsgi:application