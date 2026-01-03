from .BaseDataModel import BaseDataModel
from .db_schemes.project import ProjectDBScheme
from .enums.DataBaseEnums import DataBaseEnum

class ProjectModel(BaseDataModel):
    def __init__(self, db_client):
        super().__init__(db_client)
        self.collection = db_client[DataBaseEnum.COLLECTION_PROJECT_NAME.value]

    async def create_project(self, project: ProjectDBScheme):
        result = await self.collection.insert_one(project.model_dump())
        project._id = result.inserted_id
        return project
    