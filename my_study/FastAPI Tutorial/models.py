from sqlmodel import SQLModel, Field
from typing import Optional
from enum import IntEnum


class Priority(IntEnum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

class TodoBase(SQLModel):
    
    title: str = Field(..., min_length=3, max_length=25, description="The title of the todo")
    description: str = Field(..., min_length=15, max_length=100, description="The description of the todo")
    priority: Priority = Field(default=Priority.LOW, description="The priority of the todo")

class Todo(TodoBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, description="The id of the todo")


class TodoCreate(TodoBase):
    pass

class TodoUpdate(SQLModel):
    title: Optional[str] = Field(None, min_length=3, max_length=25, description="The title of the todo")
    description: Optional[str] = Field(None, min_length=15, max_length=100, description="The description of the todo")
    priority: Optional[Priority] = Field(None, description="The priority of the todo")

class DeleteResponse(SQLModel):
    message: str