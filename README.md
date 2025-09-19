# Remote Patient Monitoring with Voice Check-ins 📞🏥

A full-stack Django + React + Twilio app for **remote patient monitoring**.  
Patients receive **automated voice calls** asking about their health and respond with keypad or speech.  
Responses are saved in the backend and visible to doctors via a dashboard.

---

## 🚀 Features
- Automated **voice check-ins** with Twilio Programmable Voice
- Patients can respond via **speech or DTMF keypad**
- Django backend with patient + check-in models
- React frontend dashboard for monitoring and triggering calls
- API to manually trigger calls or schedule via cron
- Admin panel for managing patients
- Extensible for AI analysis of responses

---

## 🛠️ Tech Stack
- **Backend**: Django REST Framework
- **Frontend**: React + Axios
- **Telephony**: Twilio Programmable Voice
- **Database**: SQLite (dev) / Postgres (prod)
- **Deployment**: Docker (optional)

---

## ⚙️ Setup

### 1. Backend
```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
