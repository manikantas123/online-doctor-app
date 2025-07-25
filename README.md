# Online Doctor Consultation App

This app allows users to input symptoms and receive consultation responses. Built with Flask, Dockerized, deployed with Kubernetes and GitHub Actions.

## Features
- REST API for doctor consultations
- CI/CD with GitHub Actions
- Containerized with Docker
- Deployable to GKE (Google Kubernetes Engine)

## Run locally

```bash
docker build -t online-doctor-app .
docker run -p 8000:8000 online-doctor-app
