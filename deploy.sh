#!/bin/bash

deploy_docker() {
  cd $(git rev-parse --show-toplevel) && COMMIT_HASH=$(git rev-parse --short HEAD)
  export DOCKER_USERNAME="$1"
  export DOCKER_PASSWORD="$2"
  docker build -t python-oc-lettings-fr:$COMMIT_HASH -f Dockerfile .
  docker login -u "$DOCKER_USERNAME" -p "$DOCKER_PASSWORD"
  docker push $DOCKER_USERNAME/python-oc-lettings-fr:$COMMIT_HASH
  docker pull $DOCKER_USERNAME/python-oc-lettings-fr:$COMMIT_HASH
}

echo "Entrez votre nom d'utilisateur Docker : "
read DOCKER_USERNAME
echo "Entrez votre mot de passe Docker : "
read -s DOCKER_PASSWORD

deploy_docker "$DOCKER_USERNAME" "$DOCKER_PASSWORD"

