What is an API?

API (Application Programming Interface) is a way for two applications to communicate with each other.

Think of it like a waiter in a restaurant:

Client (You)
    |
    v
 API (Waiter)
    |
    v
Application/Database (Kitchen)

You send a request, and the API returns a response.

Example API
Suppose a website wants to get a list of users.

Request:

GET /users

Response:
JSON
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

The API acts as a bridge between the client and the backend.

How to Create an API

Using Python and the Flask framework:

How to Create an API

Using Python and the Flask framework:

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/list')
def get_list():
    return jsonify(["apple", "banana", "orange"])

app.run(host='0.0.0.0', port=8080)

Start the application:

python app.py
Now if you visit:

http://localhost:8080/list

You get:

["apple","banana","orange"]

How Does https://<url>:8080/list Work?

Let's break it down:

https://myapp.example.com:8080/list

1. Protocol
https://

Tells the browser to use HTTPS (encrypted communication).

2. Domain Name
myapp.example.com

The browser asks DNS:

"What IP address belongs to myapp.example.com?"

DNS replies:

54.210.100.25

3. Port
:8080

A server can run multiple services.

Example:

Port 80   -> HTTP
Port 443  -> HTTPS
Port 8080 -> Application Server
Port 3306 -> MySQL

Port 8080 tells the OS which application should receive the request.

4. Path
/list

The web server forwards the request to the /list endpoint.

Example:
@app.route('/list')

Complete Flow

Browser
  |
  | GET https://myapp.example.com:8080/list
  |
  v
DNS Lookup
  |
  v
54.210.100.25
  |
  v
Server Port 8080
  |
  v
Flask Application
  |
  v
/list Endpoint
  |
  v
JSON Response
  |
  v
Browser Displays Data

How This Works in EKS

In Kubernetes/EKS, the request often goes through:

User
  |
  v
ALB (AWS Load Balancer)
  |
  v
Ingress
  |
  v
Service
  |
  v
Pod
  |
  v
Application API (/list)

For example:

https://api.company.com/list

1. DNS points to an ALB.
2. ALB forwards traffic to the Ingress Controller.
3. Ingress routes /list.
4. Kubernetes Service finds a pod.
5. The pod executes the API code and returns data.

## What is an API?

**API (Application Programming Interface)** is a way for two applications to communicate with each other.

Think of it like a waiter in a restaurant:

```text
Client (You)
    |
    v
 API (Waiter)
    |
    v
Application/Database (Kitchen)
```

You send a request, and the API returns a response.

---

## Example API

Suppose a website wants to get a list of users.

Request:

```http
GET /users
```

Response:

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

The API acts as a bridge between the client and the backend.

---

## How to Create an API

Using Python and the Flask framework:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/list')
def get_list():
    return jsonify(["apple", "banana", "orange"])

app.run(host='0.0.0.0', port=8080)
```

Start the application:

```bash
python app.py
```

Now if you visit:

```text
http://localhost:8080/list
```

You get:

```json
["apple","banana","orange"]
```

---

## How Does `https://<url>:8080/list` Work?

Let's break it down:

```text
https://myapp.example.com:8080/list
```

### 1. Protocol

```text
https://
```

Tells the browser to use HTTPS (encrypted communication).

---

### 2. Domain Name

```text
myapp.example.com
```

The browser asks DNS:

> "What IP address belongs to myapp.example.com?"

DNS replies:

```text
54.210.100.25
```

---

### 3. Port

```text
:8080
```

A server can run multiple services.

Example:

```text
Port 80   -> HTTP
Port 443  -> HTTPS
Port 8080 -> Application Server
Port 3306 -> MySQL
```

Port 8080 tells the OS which application should receive the request.

---

### 4. Path

```text
/list
```

The web server forwards the request to the `/list` endpoint.

Example:

```python
@app.route('/list')
```

---

## Complete Flow

```text
Browser
  |
  | GET https://myapp.example.com:8080/list
  |
  v
DNS Lookup
  |
  v
54.210.100.25
  |
  v
Server Port 8080
  |
  v
Flask Application
  |
  v
/list Endpoint
  |
  v
JSON Response
  |
  v
Browser Displays Data
```

---

## How This Works in EKS

In Kubernetes/EKS, the request often goes through:

```text
User
  |
  v
ALB (AWS Load Balancer)
  |
  v
Ingress
  |
  v
Service
  |
  v
Pod
  |
  v
Application API (/list)
```

For example:

```text
https://api.company.com/list
```

1. DNS points to an ALB.
2. ALB forwards traffic to the Ingress Controller.
3. Ingress routes `/list`.
4. Kubernetes Service finds a pod.
5. The pod executes the API code and returns data.

---


An API is an interface that allows applications to communicate using requests and responses, usually over HTTP/HTTPS. To create an API, we define endpoints such as `/list` or `/users` in a backend framework like Flask, FastAPI, Spring Boot, or Node.js. When a user accesses a URL like `https://myapp.example.com:8080/list`, DNS resolves the domain name to an IP address, the request reaches the server on port 8080, and the application handles the `/list` endpoint and returns a response, typically in JSON format.

