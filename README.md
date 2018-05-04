# Python-RESTful-service-with-Docker

Created a Python RESTful services using Flask and use docker to run this application.

Docker Installation, install Dockertoolbox for windows: https://docs.docker.com/toolbox/toolbox_install_windows/ 

After installling Docker, you will get Docker terminal. :+1:

## Web App Content:
- Made data model using JSON
- Created a application using Python and Flask web framework
- Created Docker container for the application. Create Docker file for that.
- Displayed list of movies with its detail using HTML
- Displayed list of movies based on ID and Release(Year) number

## Executing the Web App Using Docker Terminal:
- Go inside web app folder in the terminal
- Build the image flass-app : docker build -t flask-app:latest . 
- Run flask-app in the Docker container : docker run -d -p 5000:5000 flask-app
  - Now this App will run on this address locally and display all list of data: http://192.168.99.100:5000/data
  - And it will display data per id or year : http://192.168.99.100:5000/data/5 OR http://192.168.99.100:5000/data/2017
- List of all images : docker images
- To check running container inside the Docker: docker ps

The internal port 5000 with the host port 5000 (-p 5000:5000)

#### Some Useful Docker Command:
- To remove Container: docker rmi -f hello-world 
- List all containers (only IDs): docker ps -aq
- Stop all running containers: docker stop $(docker ps -aq)
- Remove all containers: docker rm $(docker ps -aq)
- Remove all images: docker rmi $(docker images -q)








