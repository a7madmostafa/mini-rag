# Upload File Endpoint

1- Create a POST endpoint `/api/v1/data/upload/{project_id}` in `data.py` to handle file uploads.

* This endpoint accepts a file and a project ID as path parameter.
* It uses `UploadFile` from FastAPI to handle file uploads efficiently.
* It returns the project ID and the uploaded file name as a JSON response.

2- In `src/.env` and `src/helpers/config.py`, we set `FILE_ALLOWED_TYPES` and `MAX_FILE_SIZE_MB` for file upload constraints.

3- Create a `DataController` class in `src/controllers/DataController.py` to handle file validation logic.

4- Implement the `validate_uploaded_file` method in `DataController` to check file type and size.

5- Update the `upload_data` endpoint in `data.py` to use `DataController` for file validation before processing the upload.

6- Prepare `src/assets/files` directory to store uploaded files temporarily during testing.

7- Use `ProjectController` to get project path based on project ID for file storage.
