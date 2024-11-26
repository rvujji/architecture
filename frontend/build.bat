docker stop nodejs-container
docker rm -f nodejs-container
docker build -t frontend .
docker run -d --name nodejs-container -p 3000:3000 frontend

:: http://localhost:3000

:: docker start nodejs-container

:: docker-compose up -d