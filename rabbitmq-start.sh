#!/bin/bash

rabbitmq-server &
sleep 60
rabbitmqctl status
# rabbitmqctl add_user guest guest
rabbitmqctl set_user_tags guest administrator
rabbitmqctl add_vhost localhost
# rabbitmqctl set_permissions -p localhost guest ".*" ".*" ".*"
rabbitmqctl set_permissions -p / guest ".*" ".*" ".*"

