#!/bin/bash

ECS_CONTEXT="myecscontext"
PROJECT_NAME="bhp" # only letters and numbers here - ecs limitation

on_error() {
  echo "$1"
  exit 1
}

check_ecs_docker_context() {
  var=$(docker context list | grep ecs | grep "$ECS_CONTEXT ")
  [ -z "$var" ] && on_error "Error: docker ECS context not set or incorrect"
}

build_production_images() {
  docker-compose -p $PROJECT_NAME -f docker-compose-prod.yml build || on_error "Error: docker-compose prod build"
}

push_production_images() {
  # If error here, check if you are logged in docker hub
  docker-compose -p $PROJECT_NAME -f docker-compose-prod.yml push || on_error "Error: docker-compose prod push"
}

up_production_images_on_ecs() {
  docker --context $ECS_CONTEXT compose -p $PROJECT_NAME -f docker-compose-aws.yml up || on_error "Error: couldn't deploy to ECS"
}

down_production_images_on_ecs() {
  docker --context $ECS_CONTEXT compose -p $PROJECT_NAME -f docker-compose-aws.yml down || on_error "Error: couldn't tear down on ECS"
}

start() {
    echo "==== Start"
    check_ecs_docker_context
    build_production_images
    push_production_images
    up_production_images_on_ecs
    echo "Success"
}

stop() {
    echo "==== Stop"
    check_ecs_docker_context
    down_production_images_on_ecs
    echo "Success"
}

case "$1" in
    'up')
            start
            ;;
    'down')
            stop
            ;;
    *)
            echo
            echo "Usage: $0 { up | down }"
            echo
            exit 1
            ;;
esac

exit 0
