from fastapi import FastAPI, Query, Depends, status
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager
from typing import List
from helper import find_todo_by_id
from models import Todo, TodoCreate, TodoUpdate, Priority, DeleteResponse
from database import create_db_and_tables, get_session
from sqlmodel import Session, select


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    create_db_and_tables()
    yield

    # Shutdown 
    # the session will be closed automatically after the request

app = FastAPI(lifespan=lifespan)

# localhost:8000
@app.get("/") 
def index():
    return {"message": "Hello World"}

# localhost:8000/todos?first_n=2
@app.get("/todos", response_model=List[Todo])
def get_todos(first_n: int = Query(default=None, gt=0), session: Session = Depends(get_session)):   # Pydantic validates the type and raises an error if invalid
    query = select(Todo)
    if first_n:
        query = query.limit(first_n)
    todos = session.exec(query).all()
    return todos

# localhost:8000/todos/1
@app.get("/todos/{id}", response_model=Todo)
def get_todo(id: int, session: Session = Depends(get_session)):
    todo = find_todo_by_id(id, session)
    return todo

@app.post("/todos", response_model= Todo)
def create_todo(new_todo: TodoCreate, session: Session = Depends(get_session)):
    todo = Todo.from_orm(new_todo)
    session.add(todo)
    session.commit()
    session.refresh(todo)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=todo.dict())


@app.put("/todos/{id}", response_model=Todo)
def update_todo(id: int, updated_todo: TodoUpdate, session: Session = Depends(get_session)):
    todo = find_todo_by_id(id, session)

    # Update only fields that were provided
    updated_data = updated_todo.model_dump(exclude_unset=True)
    for key, value in updated_data.items():
        setattr(todo, key, value)  # mutate the DB object directly

    session.add(todo)
    session.commit()
    session.refresh(todo)  # refresh to get latest state from DB
    return todo

@app.delete("/todos/{id}", response_model=DeleteResponse)
def delete_todo(id: int, session: Session = Depends(get_session)):
    todo = find_todo_by_id(id, session)
    session.delete(todo)
    session.commit()
    return DeleteResponse(message=f"Todo {id} deleted successfully")