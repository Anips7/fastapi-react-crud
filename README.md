# 📦 FastAPI + React Full Stack CRUD App

## 🚀 Overview

This is a full-stack Product Management application built using:

- ⚡ FastAPI (Backend)
- 🐘 PostgreSQL (Database)
- 🧠 SQLAlchemy ORM
- ⚛️ React.js (Frontend)
- 🌐 Axios (API communication)

The application allows users to:

- Create products
- View all products
- Update products
- Delete products
- Search, sort, and filter products

---

## 🏗️ Project Structure



fastapi-react-crud/
│
├── database.py
├── database_models.py
├── models.py
├── main.py
│
├── frontend/
│ ├── src/
│ ├── package.json
│
├── .gitignore
└── README.md


---

## ⚙️ Backend Setup (FastAPI)

### 1️⃣ Create Virtual Environment

```bash
python -m venv myenv
myenv\Scripts\activate

2️⃣ Install Dependencies
pip install fastapi uvicorn sqlalchemy psycopg2-binary


(Optional)

pip install python-dotenv

3️⃣ Run Backend Server
uvicorn main:app --reload


Backend runs on:

http://localhost:8000


Swagger Docs:

http://localhost:8000/docs

🐘 PostgreSQL Setup

Make sure PostgreSQL is running.

Create database:

CREATE DATABASE fastapi_db;


Update database.py:

db_url = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/fastapi_db"

⚛️ Frontend Setup (React)
1️⃣ Go to frontend folder
cd frontend

2️⃣ Install dependencies
npm install

3️⃣ Start React App
npm start


Frontend runs on:

http://localhost:3000

🔌 API Endpoints
Method	Endpoint	Description
GET	/products	Get all products
GET	/products/{id}	Get product by ID
POST	/products	Create product
PUT	/products/{id}	Update product
DELETE	/products/{id}	Delete product
🧠 Features Implemented
Backend

SQLAlchemy ORM integration

PostgreSQL database

Dependency Injection

Proper HTTP status codes

Response models

CORS configuration

Frontend

Axios API integration

Controlled forms

Edit mode

Sorting

Filtering

Loading state

Success & error messages

Confirmation before delete

🔒 CORS Configuration
allow_origins=["http://localhost:3000"]


Ensures frontend can communicate with backend.

📈 Tech Stack

FastAPI

SQLAlchemy

PostgreSQL

React

Axios

JavaScript (ES6+)

Python 3.11+

🧑‍💻 Author

Anips Kumar Jena
GitHub: https://github.com/Anips7

🎯 Future Improvements

JWT Authentication

Pagination

Docker Support

Environment variable management

Deployment (Render / Railway / Vercel)

🌟 Status

✅ Fully functional CRUD application
✅ Database integrated
✅ Full stack connected


---

# 🚀 After Replacing

Run:

```bash
git add README.md
git commit -m "Fixed README formatting"
git push


Now GitHub will render it beautifully with:

Proper headings

Code blocks

Tables

Clean structure
