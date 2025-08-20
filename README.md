# 👕 Flask T-Shirt Store

A simple e-commerce demo built with **Flask** — product listing, cart flow, and a small checkout flow.  
This project is a learning/freelance-ready app (templates + server logic) and is deployed on **Render**.

**Live demo**: [Link!](https://flask-tshirt-store.onrender.com)  <!-- replace with your Render URL -->

---

## 🚀 Key Features
- Product catalog and product detail pages  
- Add to cart / view cart / remove items  
- Simple checkout form (client-side validation)  
- Server-side templates using Flask (`templates/`) and lightweight data models.  
- Designed to be easy to extend (payments, auth, admin) for real projects

> The repo includes core Flask files such as `app.py`, `models.py`, `requirements.txt` and a `Procfile`. :contentReference[oaicite:1]{index=1}

---

## 📁 Repo structure (high level)
```
flask-tshirt-store/
├─ app.py
├─ models.py
├─ requirements.txt
├─ Procfile
├─ templates/
├─ instance/ # local DB / config
└─ static/ # images, css, js
```

---

## 🧰 Tech stack
- Python 3.x, Flask  
- Jinja2 templates, Bootstrap (or custom CSS)  
- SQLite (local) or replace with any DB for production  
- Deployed on **Render** (web service)

---

## 🔁 Run locally

1. Clone:
```
git clone https://github.com/Yaswanth876/flask-tshirt-store.git
cd flask-tshirt-store
```

# Create virtual environment & install:
```
python -m venv venv
```
# Windows
```
venv\Scripts\activate
```
# macOS / Linux
```
source venv/bin/activate
```
```
pip install -r requirements.txt
```

(Optional) Create instance folder / DB:

mkdir instance
# if the app expects an sqlite file, create or let the app create it automatically


Set environment variables and run:

# Linux / macOS
export FLASK_APP=app.py
export FLASK_ENV=development
export SECRET_KEY='a-secure-key'   # replace for real use

flask run
# or (if app uses host/port)
```
python app.py
```

Open http://127.0.0.1:5000 in your browser.

---

### ⚙️ Deploying to Render

Connect your GitHub repo to Render and create a Web Service.

Build command (Render):

pip install -r requirements.txt


Start command (Render):

gunicorn app:app --bind 0.0.0.0:$PORT


(Assumes your Flask app object is named app in app.py — adjust if different.)
4. Add environment variables on Render (SECRET_KEY, any DB URL).
5. Deploy — Render will build and serve your app.

---

### 🛠️ Notes & Next improvements

Add user auth + admin panel to manage products

Integrate payment gateway (Stripe/Razorpay) for checkout

Replace SQLite with PostgreSQL / managed DB for production

Add unit tests and CI (GitHub Actions)

Add product images in static/ and optimize for CDN

---

### 📸 Screenshots

![Add a screenshot](home.png)

---

### 🤝 Contributing

PRs welcome — add a small description of changes and include screenshots for UI work.

---

### 👨‍💻 Author

- **Yaswanth V** 
— B.E. CSE (AI & ML), Thiagarajar College of Engineering
- [GitHub](https://github.com/Yaswanth876)
- [LinkedIn](www.linkedin.com/in/yaswanthv876)
- Contact: vsyaswanth008@gmail.com
