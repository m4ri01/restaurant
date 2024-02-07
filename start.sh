#!/bin/bash
echo "Copying .env file..."
cp .env backend/.env
cp .env frontend/.env
echo "up docker image"
docker-compose up -d --build

echo "completed!!"
