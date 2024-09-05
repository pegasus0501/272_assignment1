# 272_assignment1

# Project Structure

- **Hello Folder**: Contains `hello.py`, Dockerfile, and requirements file.
- **World Folder**: Contains `world.py`, Dockerfile, and requirements file.
- **Hello World Folder**: Contains `helloworld.py`, Dockerfile, and requirements file.
- **Yaml Files Folder**: Contains deployment and service files for hello, world, and hello world microservices.

---

# Prerequisites

- Install Git
- Create a GitHub repository
- Install and set up Docker
- Create a Kubernetes cluster on Google Kubernetes Engine

---

# Running Local Microservices

### Commands to run hello, world, and helloworld scripts locally:

#### Hello:
- Run: `python hello.py`
- Access at: `http://127.0.0.1:5004/hello`

#### World:
- Run: `python world.py`
- Access at: `http://127.0.0.1:5005/world`

---

# Building and Running Docker Images

### Build Docker images for hello and world:

- Hello: `docker build -t hello .`
- World: `docker build -t world .`
  
Verify with: `docker images`

### Run Docker images:

- Hello: `docker run -p 5004:5004 hello`
- World: `docker run -p 5005:5005 world`

---

# Pushing Docker Images to DockerHub

### Tag and push Docker images:

#### Hello:
- Tag: `docker tag hello <dockerhub-username>/hello:v1.0`
- Push: `docker push <dockerhub-username>/hello:v1.0`

#### World:
- Tag: `docker tag world <dockerhub-username>/world:v1.0`
- Push: `docker push <dockerhub-username>/world:v1.0`

---

# Deploying on Google Kubernetes Engine

### Steps:

1. Authorize: `gcloud auth login`
2. Select project: `gcloud config set project <project-id>`
3. Select cluster: `gcloud container clusters get-credentials <cluster-name> --zone <zone> --project <your-project-id>`

### Apply Deployment and Service YAML Files:

#### Hello:
- `kubectl apply -f hello-deployment.yaml`
- `kubectl apply -f hello-service.yaml`

#### World:
- `kubectl apply -f world-deployment.yaml`
- `kubectl apply -f world-service.yaml`

### Verify with:
- `kubectl get deployments`
- `kubectl get services`

Access services at:
- **Hello**: `http://34.134.245.100/hello`
- **World**: `http://34.29.141.164/world`

---

# Helloworld Microservice

### Build and push helloworld image:

- Build: `docker build -t helloworld .`
- Tag: `docker tag helloworld <dockerhub-username>/helloworld:v1.0`
- Push: `docker push <dockerhub-username>/helloworld:v1.0`

### Apply Deployment and Service YAML Files:

- `kubectl apply -f helloworld-deployment.yaml`
- `kubectl apply -f helloworld-service.yaml`

### Verify with:
- `kubectl get deployments`
- `kubectl get services`

Access at: `http://35.232.149.26/helloworld`

---
# Images of hello, world and helloworld microservices after deploying them on kubernetes

- Hello service: 
<img width="607" alt="hello-capture" src="https://github.com/user-attachments/assets/e546d826-a2b4-41a8-a69e-c04785d94256">

- World service: 

<img width="671" alt="world-Capture" src="https://github.com/user-attachments/assets/cfc046fc-6545-41ca-9860-6e793047144e">

- Hello World service: 

<img width="902" alt="helloworld-capture" src="https://github.com/user-attachments/assets/c49f63cf-f30b-477d-8153-900db42cc940">

---
# Docker Image Links

- [Hello Image](https://hub.docker.com/repository/docker/likhitmonavarthy0501/hello/general)
- [World Image](https://hub.docker.com/repository/docker/likhitmonavarthy0501/world/general)
- [Helloworld Image](https://hub.docker.com/repository/docker/likhitmonavarthy0501/helloworld/general)

---

# Service URLs

Below are the URLs to access hello, world and helloworld services:

- **Hello Service**: [http://34.134.245.100/hello](http://34.134.245.100/hello)
- **World Service**: [http://34.29.141.164/world](http://34.29.141.164/world)
- **HelloWorld Service**: [http://35.232.149.26/helloworld](http://35.232.149.26/helloworld)


---
This `README.md` provides a clear guide on setting up and running the microservices.
