# 📦 NEXIS LOGIX – Smart Inventory Management System

A modern, secure, and responsive **Inventory Management System (IMS)** built with **Django**. NEXIS LOGIX helps businesses efficiently manage products, inventory, and user profiles through a clean dashboard and production-ready architecture.

---

## Live Demo

**🌐 Live Website:** https://nexis-logix.onrender.com

---

## 📸 Features

### 🔐 Authentication

* Secure user registration and login
* Logout functionality
* Profile management
* Profile image upload with Cloudinary
* Password protection using Django Authentication
* Protected routes with `login_required`

### 📦 Inventory Management

* Add new products
* View product list
* Update product information
* Delete products
* Search and manage inventory efficiently

### 🎨 User Experience

* Responsive design for desktop and mobile
* Modern Bootstrap 5 interface
* Clean dashboard
* Dark-themed UI
* User-friendly navigation

### ☁️ Production Features

* PostgreSQL database
* Cloudinary image storage
* Render deployment
* WhiteNoise static file serving
* Environment variable configuration using `python-decouple`

---

## 🛠 Tech Stack

### Backend

* Python
* Django

### Frontend

* HTML5
* CSS3
* Bootstrap 5
* JavaScript

### Database

* PostgreSQL (Production)
* SQLite3 (Development)

### Cloud & Deployment

* Render
* Cloudinary
* WhiteNoise

---

## 📂 Project Structure

```
nexis-logix/
│── authApp/
│── invApp/
│── invProject/
│── media/
│── manage.py
│── requirements.txt
│── README.md
```

---

## ⚙️ Local Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sagur0239/nexis-logix.git
cd nexis-logix
```

### 2. Create Virtual Environment

#### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key

DEBUG=True

DATABASE_URL=your_database_url

CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### 5. Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000
```

---

## 🔒 Security

* Django Authentication System
* CSRF Protection
* Environment Variables
* Login Required Views
* Secure Password Hashing
* Cloud-based Media Storage
* Production-ready Configuration

---

## 📦 Deployment

The project is successfully deployed on **Render** with:

* PostgreSQL Database
* Cloudinary Media Storage
* WhiteNoise Static Files
* Environment Variables
* Gunicorn

---

## 👨‍💻 Developer

**Md Sagur Ali**

* GitHub: https://github.com/sagur0239
* LinkedIn: https://www.linkedin.com/in/md-sagur-ali-18a175354/

---

## 📄 License

This project is licensed under the **MIT License**.
