# Project Overview

This document provides a short summary of the applications that make up this project and the key packages used.

## Applications

### accounts
- Handles custom user registration, login and profile management.
- Key model: `UserAccount` (email based user).
- Utilises `djoser` and `templated_mail` for activation and password reset emails.

### api
- Provides standard API endpoints and user related views.
- Key model: `CustomUser` which extends Django's `AbstractUser`.
- Uses DRF viewsets and JWT authentication.

### ec_app
- Implements simple e-commerce features such as products and orders.
- Key models include `Customer`, `CustomerProfile`, `Order`, `Product`, `Category` and `ProductCategory`.
- Exposes CRUD endpoints through DRF `ModelViewSet` classes.

## Packages

Main packages referenced by the project include:
- **Django** and **Django REST framework** for the core framework.
- **dj_rest_auth** and **djangorestframework-simplejwt** for authentication.
- **djoser** for additional user management utilities.
- **django-cors-headers** for CORS handling.
- **drf-yasg** for API documentation.
- **django-extensions** and **debug_toolbar** for development support.
- **social-auth-app-django** for social authentication.
