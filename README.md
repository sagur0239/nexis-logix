# 📦 NEXIS LOGIX — Autonomous Asset & Inventory Matrix

NEXIS LOGIX is a high-performance, enterprise-grade **Inventory Management System (IMS)** built with Django and Bootstrap 5. It features a futuristic cyber-dark aesthetic designed for seamless stock tracking, real-time data asset management, and secure administrative control.

---

## ✨ Key Features
* **Secure Authentication Deck:** Custom-designed log-in architecture preventing back-button caching bypasses.
* **CRUD Matrix:** Full capability to Create, Read, Update, and Delete products and assets seamlessly.
* **Intelligent Inventory Flows:** Responsive control decks optimized for both desktop and mobile operations.
* **Cyber-Dark UI:** Glassmorphic design integrations utilizing premium typefaces (`Plus Jakarta Sans`) and smooth hover mechanics.

---

## 🛠️ Tech Stack & Architecture
* **Backend Framework:** Django (Python)
* **Frontend Interface:** HTML5, CSS3, JavaScript (ES6+), Bootstrap 5
* **Database Engine:** SQLite3 (Local Environment)

---

## Local Installation & Setup Guide

Follow these sequential steps to fire up the engine on your local terminal:

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_USERNAME/nexis-logix.git](https://github.com/YOUR_USERNAME/nexis-logix.git)
cd nexis-logix

# On Linux / Ubuntu
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

Now, open your preferred secure terminal browser and navigate to: http://127.0.0.1:8000/

🛑 Security & Optimization Configurations
Anti-Cache Loop Scripting: Implemented advanced front-end parameters (window.onpageshow) preventing unauthorized views during backward terminal logs.

View-Level Guards: Every structural Class-Based View (CreateView, UpdateView, ListView) is locked behind Django LoginRequiredMixin and never_cache decorators.

📄 License
Distributed under the MIT License. See LICENSE for more operational information.
