# Project Description - MOUDLE 12

## What is ToriloShop?
ToriloShop is a Django-based e-commerce web application that allows users to manage products and categories.  
The project demonstrates Django fundamentals such as models, views, templates, forms, CRUD operations, media handling, admin customization, and user authentication.

The application includes product images, custom styling, search functionality, protected routes, and permission-based access control for staff users.

### What does it do?
The application allows users to create, view, update, search, and manage products and categories through a functional web interface.

It supports product image uploads, customised admin features, and authentication functionalities such as registration, login, and logout.

Authenticated users can access protected product management pages, while only staff users are allowed to delete products.

The navigation bar also updates dynamically depending on whether the user is logged in or logged out.

# ToriloShop - Django CRUD Project

## Project Description

ToriloShop is a Django-based e-commerce project that allows users to manage products and categories.  
It supports full CRUD operations:

- Create products and categories
- Read (view) product and category lists
- Update product and category details
- Delete products and categories safely

It also includes:
- Search functionality for products
- Form validation
- Success messages after actions


## Django Authentication Project

## Features Implemented

### Authentication Features

- User Registration  
  URL: `/accounts/register/`  
  ➜ Allows users to create a new account using username, email, and password.

- User Login  
  URL: `/accounts/login/`  
  ➜ Allows registered users to login securely.

- User Logout  
  URL: `/accounts/logout/`  
  ➜ Logs users out and redirects them to the homepage.


### Protected Product Features

- Protected Add Product  
  URL: `/products/add/`  
  ➜ Only logged-in users can access the add product page.

- Protected Edit Product  
  URL: `/products/<id>/edit/`  
  ➜ Only authenticated users can edit products.

- Staff Only Delete Product  
  URL: `/products/<id>/delete/`  
  ➜ Only staff users are allowed to delete products.


### Navbar Authentication Features

- Logged In Navbar  
  ➜ Displays username and logout button when user is authenticated.

- Logged Out Navbar  
  ➜ Displays login and register links when user is not authenticated.


## Setup Instructions

Follow these steps to run the project locally:

### 1. Open your terminal or command prompt using

   C + ` (shortcut)

### 2. Navigate to the project folder:

   `cd/chinenye-osondu-backend-dune-cohort/Assignment-solution/module-12/toriloshop`

### 3. Create a virtual environment:

   `python -m venv venv`

### 4. Activate the virtual environment:

#### Windows

   `venv\Scripts\activate`

### 5. Install Django:

   `pip install django`

### 6. Run migrations:

   `python manage.py makemigrations`

**Then Type**

   `python manage.py migrate`

### 7. Create superuser:

   `python manage.py createsuperuser`

### 8. Run the server:

   `python manage.py runserver`

### 9. Open in browser(Use this link):

   `http://127.0.0.1:8000/`

### 10. Use this to Access admin panel:

   `http://127.0.0.1:8000/admin/`


## Screenshots

### Staff User Delete Access Page
![Staff User Delete Access Page](screenshots/21_staff_user_delete_access.png)

### Registration Page
![Registration Page](screenshots/22_registration_page.png)

### Login Page For Registered Users
![Login Page For Registered Users](screenshots/23_login_page.png)

### Customer's Registration Page
![Customer's Registration Page](<screenshots/24_customer's registration.png>)

## Conclusion

This project demonstrates the fundamentals of Django web development, including models, views, templates, forms, CRUD operations, media handling, admin customization, and user authentication.

The application allows users to manage products and categories, upload product images, perform search operations, and access protected routes securely.

It also demonstrates how to implement authentication features such as registration, login, logout, permission-based access control, and dynamic navigation updates based on user authentication status.

Overall, ToriloShop serves as a foundation for building more advanced and secure e-commerce web applications using Django.