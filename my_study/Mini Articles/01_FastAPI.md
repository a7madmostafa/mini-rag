# Fast API

## First Steps
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
def welcome():
    return {"message": "Hello World"}
```
## Running the Application
To run the FastAPI application, use the following command:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
* `main`: Refers to the Python file name (main.py).
* `app`: Refers to the FastAPI instance created in the file.
* `--reload`: Enables auto-reload for code changes during development (Not recommended for production).
* `--host 0.0.0.0`: Makes the server accessible from any IP address.
* `--port 5000`: Sets the port number to 5000.

## Accessing the Application
Once the server is running, you can access the application by navigating to `http://127.0.0.1:8000/welcome`.
You should see a JSON response:
```json
{
    "message": "Hello World"
}
```
## Testing the Endpoint with curl
You can test the endpoint using `curl` from the command line:
```bash
curl http://127.0.0.1:8000/welcome
```
You should receive the following response:
```json
{
    "message": "Hello World"
}
```

## Testing the Endpoint with Python
You can also test the endpoint using Python:
```python
import requests

response = requests.get('http://127.0.0.1:8000/welcome')
print(response.json())
```
You should see the output:
```json
{   
     "message": "Hello World"
}
```

## Testing the Endpoint with Swagger UI
FastAPI automatically generates an interactive API documentation using Swagger UI. You can access it by navigating to `http://127.0.0.1:8000/docs`. Here, you can see the available endpoints and test them directly from the browser.

## Testing the Endpoint with redoc
FastAPI also provides another documentation interface using ReDoc. You can access it by navigating to `http://127.0.0.1:8000/redoc`. Here, you can see the available endpoints and test them directly from the browser. 

## Testing the Endpoint with Postman
1. Open Postman and create a new GET request.
2. Enter the URL: `http://127.0.0.1:8000/welcome`
3. Click the "Send" button.
4. You should see the JSON response: `{"message": "Hello World"}`
