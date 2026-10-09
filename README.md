# docker-demo-with-cicd

A simple web application built using Python Flask ,containerized using Docker and Added CICD.

This project demonstrates how a Flask application can be packaged and run inside a Docker container.

## Technologies Used

* Python
* Flask
* HTML
* Docker
* Git
* GitHub
* GitHub Actions

## Project Structure

docker-flask-app/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
│
├── .github/workflows
│   └── action/yml

## How It Works

The application uses Flask to serve a web page.

Docker packages the Flask application together with its dependencies into a Docker image.

The Docker container runs the application and maps container port `5005` to port `5000` on the host machine.

Browser
   |
   | http://localhost:5005
   |
Docker Container
   |
Flask Application
   |
HTML 

## Run the Project Locally

### 1. Clone the repository


git clone https://github.com/NARESH838/docker-demo-with-cicd.git


Move into the project directory:


cd docker1-app


### 2. Build the Docker image


docker build -t flask-docker-app .

### 3. Run the container


docker run -d -p 5000:5000 --name flask-container flask-docker-app


### 4. Open the application

Open the following URL in your browser:


http://localhost:5000


## Docker Commands Used

Build the image:


docker build -t flask-docker-app .


Run the container:


docker run -d -p 5000:5000 --name flask-container flask-docker-app


View running containers:


docker ps


View application logs:


docker logs flask-container

 Also using docker hub 

 docker pull nareshnb357/cicd-demo

 docker run -d -p 5000:5000 --name conatiner-name nareshnb357/cicd-demo

## What I Learned

Through this project, I practiced:

* Creating a Flask web application
* Using Flask templates
* Creating a Dockerfile
* Building Docker images
* Running Docker containers
* Port mapping
* Using `.dockerignore`
* Using Git and GitHub for version control
* cicd using github actions

## Author
Naresh 
