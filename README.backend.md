Backend (Django)
----------------
- Install: pip install -r requirements.txt
- Set env vars from .env.example
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver
- Add patients in admin (or via shell)
- Trigger checks: python manage.py call_patients (use cron for schedule)
