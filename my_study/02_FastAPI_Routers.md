# Fast API Routers

We can organize our FastAPI application using routers. Routers allow us to group related endpoints together, making our code more modular and easier to maintain.

## Creating a Router
To create a router, we can use the `APIRouter` class from FastAPI. Here's an example of how to create a simple router in a separate file called `routes/base.py`:
```python
from fastapi import FastAPI, APIRouter

router = APIRouter(
    prefix="/api/v1",
    tags=["api/v1"]
)

@router.get("/")
def welcome():
    return {"message": "Welcome from the base route!"}
``` 
## Including the Router in the Main Application
Once we have created a router, we need to include it in our main FastAPI application. Here's how we can do that in `main.py`:
```pythonfrom fastapi import FastAPI
from routes.base import router

app = FastAPI()

app.include_router(router)
```
