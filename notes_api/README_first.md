# 🚀 Notes API - Python Backend Learning

> A beginner-friendly collection of notes and examples for learning REST APIs using Python, Flask, and modern backend concepts.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.x-black.svg)
![REST API](https://img.shields.io/badge/API-REST-green.svg)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

---

## 📖 Overview

This repository contains notes, examples, and explanations to help understand how REST APIs work.

### Topics Covered

- What is an API?
- Request and Response
- HTTP Methods
- URL Structure
- Flask API Development
- JSON Responses
- DNS Resolution
- HTTPS Communication
- API Flow in Kubernetes (Amazon EKS)

---

## 📂 Repository Structure

```text
notes_api/
├── app.py
├── README.md
└── requirements.txt
```

---

# 🧠 What is an API?

An **Application Programming Interface (API)** enables two software applications to communicate using HTTP requests and responses.

```text
Client
   │
   ▼
 REST API
   │
   ▼
Backend Application
   │
   ▼
 Database
```

The client sends a request, the server processes it, and the API returns a response.

---

# 🌐 Example API

### Request

```http
GET /users
```

### Response

```json
[
  {
    "id": 1,
    "name": "John"
  },
  {
    "id": 2,
    "name": "Mike"
  }
]
```

---

# 🛠 Create Your First API

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/list")
def get_list():
    return jsonify(["apple", "banana", "orange"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```

Run the application:

```bash
python app.py
```

Open:

```text
http://localhost:8080/list
```

---

# 🔍 Understanding an API URL

```text
https://api.example.com:8080/list
```

| Component | Description |
|-----------|-------------|
| https | Secure communication protocol |
| api.example.com | Domain name |
| 8080 | Server port |
| /list | API endpoint |

---

# 🌎 Complete Request Flow

```text
Browser
   │
   ▼
DNS Lookup
   │
   ▼
Server IP
   │
   ▼
Web Server
   │
   ▼
Flask Application
   │
   ▼
/list Endpoint
   │
   ▼
JSON Response
```

---

# ☸️ API Flow in Amazon EKS

```text
User
 │
 ▼
Route53
 │
 ▼
Application Load Balancer
 │
 ▼
Ingress
 │
 ▼
Kubernetes Service
 │
 ▼
Pod
 │
 ▼
REST API
 │
 ▼
Database
```

---

# 📚 Common HTTP Methods

| Method | Purpose |
|--------|---------|
| GET | Read data |
| POST | Create data |
| PUT | Replace data |
| PATCH | Update data |
| DELETE | Delete data |

---

# 📦 Common HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

---

# 🚀 Technologies

- Python
- Flask
- REST APIs
- JSON
- HTTP/HTTPS
- DNS
- Kubernetes
- Amazon EKS

---

# 🎯 Learning Outcomes

After completing these notes, you will understand:

- REST API fundamentals
- HTTP requests and responses
- URL anatomy
- Flask basics
- DNS resolution
- JSON APIs
- Kubernetes networking
- API request flow in production

---

# 🔮 Future Improvements

- FastAPI examples
- JWT Authentication
- SQLAlchemy
- Docker
- Kubernetes Deployment
- CI/CD
- Unit Testing
- Swagger / OpenAPI
- API Versioning

---

## ⭐ If you found these notes helpful, consider giving this repository a star!
