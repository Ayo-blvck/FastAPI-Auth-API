# 🚀 FastAPI Auth API

A lightweight authentication API built with FastAPI, supporting user registration, login (OAuth2 + JWT), and secure access to protected routes.

---

## 🧱 Features

- ✅ User registration
- ✅ Secure login with JWT token
- ✅ Protected `/me` route
- ✅ Password hashing (bcrypt via Passlib)
- ✅ Token expiration logic
- ✅ SQLAlchemy ORM & Alembic migrations
- ✅ Modular router structure
- ✅ PostgreSQL support

---

## 🧑‍💻 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **SQLAlchemy**
- **Alembic**
- **PostgreSQL**
- **Docker**
- **JWT (python-jose)**
- **OAuth2PasswordBearer**

---

## 📂 Project Structure

```
fastapi-auth-api/
├── app/
│   ├── main.py              # App entrypoint
│   ├── auth.py              # Auth functions: hash, JWT, token
│   ├── crud.py              # DB access functions
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── database.py          # DB setup
│   ├── config.py            # (Optional) env variable loading
│   └── routers/
│       └── user.py          # Auth and user routes
├── alembic/
│   └── versions/            # Migration scripts
├── .env                     # Environment config
├── alembic.ini              # Alembic settings
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fastapi-auth-api.git
cd fastapi-auth-api
```

### 2. Create `.env`

```env
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
DATABASE_URL=postgresql://user:password@localhost/dbname
```

### 3. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 4. Run Alembic Migrations

```bash
alembic upgrade head
```

### 5. Start the Server

```bash
uvicorn app.main:app --reload
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for Swagger UI.

---

## 🛠️ Example Endpoints

### ➕ Register

`POST /register`

```json
{
  "email": "user@example.com",
  "password": "secret123"
}
```

---

### 🔑 Get Token

`POST /token`

Form Data:

```
username=user@example.com
password=secret123
```

---

### 👤 Get Current User

`GET /me` with Header:

```
Authorization: Bearer <your_token>
```

---

## 🥪 Testing

*TODO: Add tests with pytest + httpx*

---

## 📌 To Do

-

---

## 📄 License

MIT © 2025 Martins Odunola

