#!/bin/bash

project_name=${PWD##*/}
container=$(echo ${project_name}:$(git rev-parse --short HEAD))

export_path=${1:-${project_name}.tar}

docker build . -t $container
docker export $(docker create $container) -o $export_path

echo $export_path
