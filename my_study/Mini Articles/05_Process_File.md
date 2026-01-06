# File Processing Endpoint

1- Create a POST endpoint `/api/v1/data/process/{project_id}` in `data.py` to handle file processing requests.

* This endpoint accepts a project ID as path parameter.

2- Create a `ProcessRequest` Pydantic model in `src/routes/schemes/data.py` to define the request body schema.

* The model includes:
  - `file_id` (str): ID of the file to process.
  - `chunk_size` (Optional[int]): Size of each text chunk (default: 100).
  - `overlap` (Optional[int]): Overlap size between chunks (default: 20).
  - `do_reset` (Optional[int]): Flag to reset existing chunks (default: 0).

3- Create a `ProcessController` class in `ProcessController.py` to handle the file processing logic.

4- Implement the `process_data` endpoint in `data.py` to use `ProcessController` for file processing.