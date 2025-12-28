# Docker and MongoDB

1- Install Docker

   Follow the official Docker installation guide for your operating system: [Docker Installation](https://docs.docker.com/get-docker/).

2- We will use docker compose to run the MongoDB container.

3- Create a `docker-compose.yml` file in the root directory of your project:
```yaml
services:
  mongodb:
    image: mongo:7.0.28-jammy
    container_name: mongodb
    ports:
      - "27007:27017"
    volumes:
      - ./mongodb:/data/db
    networks:
      - backend
    restart: always

networks:
  backend:
    driver: bridge
```

4- Run the MongoDB container using Docker Compose:

   ```bash
   docker-compose up -d
   ```

5- Verify that the MongoDB container is running:

   ```bash
   docker ps
   ```
    You should see the `mongodb` container listed.

6- Download studio 3T to interact with MongoDB visually: [Studio 3T Download](https://studio3t.com/download/).
7- Configure your application to connect to the MongoDB instance running in the Docker container. Update your database connection settings to use `mongodb://localhost:27007` as the connection string.
8- Test the connection to ensure your application can successfully connect to the MongoDB database.
9- You can now use MongoDB in your application for data storage and retrieval.
10- Download `PyMongo` to interact with MongoDB from Python:
11- Example of connecting to MongoDB using PyMongo:
```python
from pymongo import AsyncMongoClient
client = AsyncMongoClient("mongodb://localhost:27007")
db = client["minirag_db"]
```
12- Make sure to update your `.env` file and configuration files to include the MongoDB connection details as shown in the recent edits.

13 In `main.py`, we will use `AsyncMongoClient` with `lifespan` option in FastAPI to connect to MongoDB at startup and close the connection at shutdown.

14- In 'models.py', we will have `db_schemes` for MongoDB:
 * `data_chunk.py`
 * `project.py`