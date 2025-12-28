from .BaseController import BaseController
from .ProjectController import ProjectController
from fastapi import UploadFile
from models import ResponseStatus
import re
import os
import string
import random

class DataController(BaseController):
    def __init__(self):
        super().__init__()

    def validate_uploaded_file(self, file: UploadFile) -> bool:
        allowed_types = self.app_settings.FILE_ALLOWED_TYPES
        max_size_bytes = self.app_settings.MAX_FILE_SIZE_MB * 1024 * 1024

        if file.content_type not in allowed_types:
            return False, ResponseStatus.FILE_TYPE_NOT_SUPPORTED.value

        if file.size > max_size_bytes:
            return False, ResponseStatus.FILE_SIZE_EXCEEDED.value

        return True, ResponseStatus.FILE_UPLOAD_SUCCESS.value
    
    def generate_random_string(self, length: int = 8) -> str:
        
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def get_clean_file_name(self, file_name: str):

        # remove any special characters, except underscore and .
        cleaned_file_name = re.sub(r'[^\w.]', '', file_name.strip())

        # replace spaces with underscore
        cleaned_file_name = cleaned_file_name.replace(" ", "_")

        return cleaned_file_name
    
    def generate_unique_file_name(self, filename: str, project_id: str) -> str:
        # Generate a unique filename by appending a random string before the file extension.
        random_key = self.generate_random_string()
        project_path = ProjectController().get_project_path(project_id=project_id)
        cleaned_name = self.get_clean_file_name(filename)
        file_id = random_key + "_" + cleaned_name
        new_filename = os.path.join(project_path, file_id)
        while os.path.exists(new_filename):
            random_key = self.generate_random_string()
            new_filename = os.path.join(project_path, random_key + "_" + cleaned_name)
        return new_filename, file_id