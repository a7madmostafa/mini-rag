
from fastapi import HTTPException
from models import Todo
from sqlmodel import Session


def find_todo_by_id(id: int, session: Session) -> Todo:
    todo = session.get(Todo, id)
    if not todo:
        raise HTTPException(status_code=404, detail=f"Todo with id {id} not found")
    return todo

