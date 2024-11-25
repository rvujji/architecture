## Setup Servers
## DB docker setup
docker --version
mkdir D:/docker/mongo-data
docker pull mongo:latest
# windows
docker run -d --name mongodb-container -p 27017:27017 -v D:/docker/mongo-data:/data/db mongo:latest
# linux
# docker run -d --name mongodb-container -p 27017:27017 -v ~/mongo-data:/data/db mongo:latest
## FastAPI docker setup

## Nodejs docker setup

