from pydantic import BaseModel, Field, field_validator
from typing import Optional
from bson import ObjectId

class ProjectDBScheme(BaseModel):
    _id : Optional[ObjectId]
    project_id : str = Field(..., min_length=1)

    @field_validator("project_id")
    @classmethod
    def validate_project_id(cls, value: str) -> str:
        if not value.isalnum():
            raise ValueError("project_id must contain only letters and numbers")
        return value
    
    class Config:
        allow_population_by_field_name = True


