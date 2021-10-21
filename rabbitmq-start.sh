#!/bin/bash

rabbitmq-server &
sleep 30
rabbitmqctl status
# rabbitmqctl add_user guest guest
rabbitmqctl set_user_tags guest administrator
rabbitmqctl add_vhost my-rabbit
rabbitmqctl set_permissions -p my-rabbit guest ".*" ".*" ".*"
# rabbitmqctl set_permissions -p / guest ".*" ".*" ".*"

