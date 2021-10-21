# microservice-one

## Setup Instructions

Install Docker & Docker Compose

### To Build & Run
> docker-compose up --build -d

### To Check logs
> docker-compose logs -f ms1

### To Stop & Delete Containers & Images
> docker-compose down


> dc -f docker-compose-dev.yml up --build -d
> dc -f docker-compose-dev.yml down --remove-orphans
