BriteCore's hiring project
========================

This is an implementation of BriteCore's hiring project.

<a href="https://github.com/vchaptsev/cookiecutter-django-vue">
    <img src="https://img.shields.io/badge/built%20with-Cookiecutter%20Django%20Vue-blue.svg" />
</a>

## Requirements
- [Docker Desktop](https://hub.docker.com/signup/awsedge?utm_source=awsedge);
  - This project was built using 20.10.5 version on Mac.
- [Docker-Compose](https://docs.docker.com/compose/);
  - This project was built using 1.28.5 version on Mac.
- [Docker Hub](https://hub.docker.com/) account;
- [AWS account](https://aws.amazon.com).

## Development

Install [Docker Desktop](https://hub.docker.com/signup/awsedge?utm_source=awsedge) and [Docker-Compose](https://docs.docker.com/compose/).

Create a `.env` file in root folder.
  - There is an `env-example` file to guide you.

Start your virtual machines with the following shell command:

`docker-compose up --build`

## Deploy

The deployment for this project is based on the experimental `docker compose`
(without the `-`) and `docker context` features, using an AWS context. You can read more about it
[here](https://aws.amazon.com/blogs/containers/deploy-applications-on-amazon-ecs-using-docker-compose/).
This was definitely a shortcut, specially because I used docker hub as the
container registry, to avoid writing code to create and maintain an ECR.

To make things simple, the strategy here was to have a development compose file,
another to build and push the production images (as docker compose ecs doesn't
support `build` command) and finally one to be used with the ECS context.
The first two came with the [cookicutter](https://github.com/vchaptsev/cookiecutter-django-vue),
I had only to modify them.

### Setup

- Log into Docker Hub (`docker login`);
- Create ECS context with `docker context create ecs <YOUR CONTEXT NAME>`;
- Configure both `docker-compose-prod.yml` and `docker-compose-aws.yml` files;
  - Change the image names to use your docker hub account.
- Configure deploy.sh.
  - Ensure the `ECS_CONTEXT` variable is correct with `<YOUR CONTEXT NAME>`.

### Running

With the setup ready, you can use the `deploy.sh` script to deploy the
service to AWS. The commands are:

- `deploy.sh up` to deploy the service.
- `deploy.sh down` to tear it down.

## Deliverables

### Data:
1. ORM file [risk type models](backend/apps/risks/models.py);
2. [Entity-relationship diagram](https://dbdiagram.io/d/60591398ecb54e10c33cb77f).

### Backend

1. [Backend in Django](backend).

### Frontend

1. [Frontend in Vue](frontend).

## Live

Live instance [here](http://bhp-LoadBal-VCDD4NLMIL0Z-282533842.sa-east-1.elb.amazonaws.com).
