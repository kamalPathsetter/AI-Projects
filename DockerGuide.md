## Docker Image
 - The actual package where all the dependencies and the components exist.
 - It is an Artifact that can be moved around.
 - Image won't be running.

## Docker Container
 - Actually start the application.
 - Container environment is created.

### Command to see the running applications

`docker ps`

### Command to run the docker image on a container. For the latest version.
`docker run application_name/image_name` 

### Command to run the docker image on a container. For a specific version.
`docker run application_name/image_name:version`

## Docker vs Virtual Machine
 - So, there is 
    - Applications
    - OS Kernel
    - Hardware

- Applications run on top of OS kernel based on the Operating System.

- In Docker, we virtualize the application layer and we use the kernel of the host coz it don't have its own.

- In Virtual Machine, we virtualze bothe the application and kernel layer. This doesn't use your kernel, it uses its own.

- Docker Containers start and run much faster.

## Docker Registries
 - A store and distribution system for Docker Images.
 - Official Images available from applications like Redis, Milvus, etc.
 - Official Images are maintained by the software authors or in collaboration with Docker Community.
 - Docker hosts one of the largest registries - <b>Docker Hub</b>

## Main Docker Commands

### Pulling the existing images
`docker pull image_name`

### View all Images
`docker images`

### Run Docker Images
`docker run image_name` 

### View the running images
`docker ps`

### Run Docker Images in Detach Mode
`docker run -d image_name`

### Stop the service
`docker stop container_id`

### List running and stopped containers
`docker ps -a`

### View Logs of a Container
`docker logs container_id`

### Port Binding
 - This will accessed to us on the port mentioned by us.

 - `docker run -d -p host_port:container_port application_name/image_name:version`

 - Only **one service** can be hosted on **one port**.

### docker run
 - Creates a new container
 - Does not re-use the previous


## Structure of a Docker File
 - FROM
    - Docker files must begin with FROM instruction.
    - Build this image from the specified image.
    - `FROM python:3.11-bullseye`

 - COPY
    - Copies the files from **src** and adds them to the file system of the container at the path **dest**.
    - While **RUN** is the executed on the container, **COPY** is executed on the host.
    - `COPY requirements.txt /app/`
    - `COPY src /app/`

 - WORKDIR
    - Sets the working directory for all commands.
    - Like changing into a directory cd ..
    - `WORKDIR /app`

 - RUN
    - Will execute any command in a shell inside the container environment.
    - `RUN pip install -r requirements.txt`

 - CMD
    - The instruction which has to be executed when a Docker Container starts.
    - There can be only one **CMD** instruction in a Docker File.
    - `CMD ["python", "main.py"]`

## Build Docker Image

 - `docker build -t python-app:1.0 {Dockerfile Path}`
 - `-t or --tag` refers to the tag.
 - `docker run -d -p 8000:8000 python-app:1.0`

## Docker Compose
 - Define and run multiple services in one isolated environment.
 - `docker-compose.yaml` file
 - You use a single YAML file to configure and maintain your application's services.
 - With a single command, you create and start all the services from your configuration.

### docker-compose.yaml

`version: '3.1'` - Version of Docker Compose

`services: ` - List all the services or the containers.
   - `mongodb: `
     - `image: mongodb`
     - `ports: `
       - `27017:27017`
     - `environment: `
       - `MONGO_INITDB_ROOT_USERNAME=admin`
       - `MONGO_INITDB_ROOT_PASSWORD=pass`
   - `mongo-express: `
     - `image: mongo-express`
     - `ports: `
       - `8081:8081`
     - `environment: `
       - `ME_CONFIG_MONGODB_ADMINUSERNAME=admin`
       - `ME_CONFIG_MONGODB_ADMINPASSWORD=password`
       - `ME_CONFIG_MONGODB_SERVER`