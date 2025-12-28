# Our Project Structure

> We can start from pre-existing structures like `FastAPI Boilerplate`.

* We will organize our project into several key directories and files to maintain clarity and modularity:
* `src` directory: Contains the main Python code for the application.
* Inside `src`, we will have:
    * `assets` directory: Contains postman collections for API testing.
    * `helpers` directory: Contains utility functions and helper modules.
    * `controllers` directory: Contains route handlers for different API endpoints.
    * `models` directory: Contains data models and schemas.
    * `routes` directory: Contains route definitions for the API.


> We will also use `pydantic-settings` for managing our configuration settings in a structured way.
* `helpers/config.py`: This file will define our configuration settings using `pydantic-settings`.
```
class Settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPENAI_API_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )


def get_settings() -> Settings:
    return Settings()
```
* This approach allows us to easily manage and access our configuration settings throughout the application.

* Now, in our route handlers (e.g., `src/routes/base.py`), we can import and use the `get_settings` function to access our configuration values:
```
from helpers.config import get_settings

settings = get_settings()
app_name = settings.APP_NAME
app_version = settings.APP_VERSION
```
