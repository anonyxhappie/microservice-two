#!/bin/bash

rabbitmq-server &> output.log & disown
sleep 30
rabbitmqctl status

cd /microservice-one/
python3 project_dir/manage.py migrate
cd /microservice-two/
python3 project_dir/manage.py migrate
cd /microservice-three/
python3 project_dir/manage.py migrate

nohup python3 /microservice-one/project_dir/manage.py runserver 0.0.0.0:8000 &> output.log & disown
nohup python3 /microservice-one/project_dir/consumer.py &> output.log & disown
nohup python3 /microservice-two/project_dir/manage.py runserver 0.0.0.0:8001 &> output.log & disown
nohup python3 /microservice-two/project_dir/consumer.py &> output.log & disown
nohup python3 /microservice-three/project_dir/manage.py runserver 0.0.0.0:8002 &> output.log & disown
nohup python3 /microservice-three/project_dir/consumer.py &> output.log & disown
