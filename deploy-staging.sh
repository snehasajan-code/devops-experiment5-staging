#!/bin/bash
set -e

echo "Starting staging deployment..."

mkdir -p staging
cp app.py staging/app.py
cp Dockerfile staging/Dockerfile
cp docker-compose.yml staging/docker-compose.yml

echo "Application files copied to staging directory."
echo "Staging deployment completed successfully."
echo "Staging files:"
ls -l staging
