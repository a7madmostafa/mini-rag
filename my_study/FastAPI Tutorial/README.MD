# FastAPI Tutorial

**A separate tutorial for FastAPI using :**
- [FastAPI Full Crash Course - Python’s Fastest Web Framework](https://www.youtube.com/watch?v=rvFsGRvj9jo)

---

## What is an API?

APIs are a way for software to communicate with other software. It is all about how to get a service from other pieces of software and how to send data to other pieces of software.

## Endpoints

Endpoints are the entry points to your API. They are the URLs that your users will use to interact with your API.

## Routes vs Endpoints

* **A route is the mapping rule that tells the server:**

```
“When a request comes to this URL with this HTTP method, run this code.”
```

* **Example**

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
```
**Here**:
* `/users/{user_id}` is the route.
* `@app.get` is the decorator for `GET` HTTP method.
* `get_user(user_id: int)` is the handler function.

✅ This whole definition is the `route`.

* **An endpoint is the actual URL that clients can call to interact with your API.**

* **Example**

```
GET https://api.example.com/users/5
```
**This is an endpoint:**
* Fully resolved URL

* Used by frontend, mobile apps, Postman, curl, etc.

## Key Differences
| Aspect      | Route                        | Endpoint                  |
| ----------- | ---------------------------- | ------------------------- |
| Perspective | Server-side                  | Client-side               |
| Purpose     | Maps requests to logic       | Access point for clients  |
| Includes    | Path + HTTP method + handler | Full URL (usually)        |
| Defined in  | Backend code                 | API documentation / usage |
| Visibility  | Internal                     | Public                    |


## What is FastAPI?

+ FastAPI is a modern, high-performance web framework for building APIs with Python.

+ FastAPI is `open source` and `free to use` with a `MIT license`.

+ FastAPI is an `asynchronous` framework that uses `starlette` under the hood.

### Asynchronous Framework

![Async](async.png)

* If the execution of a task depends on the end of another task, it is called `synchronous programming`.

* If the execution of a task is not blocked by other tasks, it is called `asynchronous programming`.

## FastAPI vs Flask vs Django
### **Features Comparison:**


| Feature        | FastAPI    | Flask      | Django               |
| -------------- | ---------- | ---------- | -------------------- |
| Performance    | ⭐⭐⭐⭐⭐      | ⭐⭐⭐        | ⭐⭐                   |
| Async Support  | ✅ Native   | ⚠️ Limited | ⚠️ Partial           |
| API Docs       | ✅ Auto     | ❌ Manual   | ⚠️ Manual            |
| Validation     | ✅ Built-in | ❌ External | ⚠️ Forms/Serializers |
| ORM            | ❌          | ❌          | ✅                    |
| Admin Panel    | ❌          | ❌          | ✅                    |
| Learning Curve | Medium     | Easy       | Steep                |
| ML-Friendly    | ⭐⭐⭐⭐⭐      | ⭐⭐⭐⭐       | ⭐⭐                   |

### **Use Cases:**

| Framework   | Type                 | Best For                           |
| ----------- | -------------------- | ---------------------------------- |
| **Flask**   | Micro-framework      | Small apps, learning, full control |
| **FastAPI** | Modern API framework | High-performance APIs, ML services |
| **Django**  | Full-stack framework | Large, production-ready web apps   |


## How to Get Started with FastAPI

1- Install FastAPI:
```bash
pip install fastapi
``` 

2- Create a FastAPI application:
```python
from fastapi import FastAPI

app = FastAPI()
```

3- Define a route:
```python
@app.get("/")
async def root():
    return {"message": "Hello World"}
```

4- Run the FastAPI application:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
OR
```bash
fastapi dev main.py
```

5- Access the API at http://localhost:5000

6- Enjoy your FastAPI application!

## HTTP Methods
FastAPI supports the following HTTP methods:
* `GET`: Retrieve data from the server.
* `POST`: Create new data on the server.
* `PUT`: Update existing data on the server.
* `DELETE`: Delete data from the server.