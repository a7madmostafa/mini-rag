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

6- Download 
   ```