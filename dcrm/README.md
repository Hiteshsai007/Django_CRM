# Django CRM

<p align="center">
   <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License" />
   <img src="https://img.shields.io/badge/Python-3.10%2B-blue.svg" alt="Python" />
   <img src="https://img.shields.io/badge/Django-6.0.5-success" alt="Django" />
   <img src="https://img.shields.io/badge/PostgreSQL-Supported-blue" alt="PostgreSQL" />
</p>

# Django CRM

A simple Customer Relationship Management (CRM) web application built with Django 6.0.5. This project allows users to manage customer records, register new users, and perform CRUD operations on records through a user-friendly web interface.

## Features

- User registration and authentication
- Add, view, update, and delete customer records
- Responsive web interface with navigation
- PostgreSQL database support (via psycopg)

## Project Structure

```
manage.py
/website
    models.py        # Database models for records
    views.py         # Application logic and request handling
    urls.py          # URL routing for the app
    forms.py         # Django forms for user input
    templates/       # HTML templates (base, home, navbar, etc.)
    migrations/      # Database migrations
/dcrm
    settings.py      # Project settings
    urls.py          # Project-level URL routing
virt/                # Python virtual environment
```

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Hiteshsai007/Django_CRM.git
   cd Django_CRM
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv virt
   # On Windows:
   virt\Scripts\activate
   # On macOS/Linux:
   source virt/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(If requirements.txt is missing, install manually:)*
   ```bash
   pip install django psycopg2-binary
   ```

4. **Configure the database:**
   - Update `DATABASES` in `dcrm/settings.py` for your PostgreSQL setup.

5. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser (admin):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Usage

- Register a new user or log in with an existing account.
- Add, view, update, or delete customer records.
- Admins can access the Django admin panel at `/admin/`.

## License

This project is licensed under the MIT License.

---

*Developed by Hiteshsai007 and contributors.*
