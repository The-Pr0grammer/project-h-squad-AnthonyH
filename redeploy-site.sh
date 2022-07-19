#!/bin/bash

cd  ~/project-h-squad-AnthonyH
git fetch && git reset origin/main --hard

docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up --build