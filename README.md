# Book Catalog API
## Project Overview

This project is a complete implementation of a RESTful API for managing a book catalog. 
The API is built with the Django REST Framework, containerized using Docker, and deployed to a Kubernetes cluster. 
The entire end-to-end process is automated through a CI/CD pipeline using GitHub Actions and Argo CD for a GitOps workflow.

This project is a RESTful API for managing a catalog of books, built with Django and deployed to a Kubernetes cluster using a fully automated CI/CD pipeline.
API Usage Examples

The API provides standard CRUD (Create, Read, Update, Delete) endpoints for managing books.

### List All Books

curl http://<YOUR_APP_URL>/api/books/

### Create a New Book

curl -X POST \
-H "Content-Type: application/json" \
-d '{"title": "Dune", "author": "Frank Herbert", "isbn": "9780441013593", "published_date": "1965-08-01"}' \
http://<YOUR_APP_URL>/api/books/

### Retrieve a Specific Book

curl CURL COMMAND HERE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

### Update a Book (Partial)

curl CURL COMMAND HERE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

### Delete a Book

curl CURL COMMAND HERE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# Local Development Setup
## Prerequisites

    Docker

    Docker Compose

## Running the Application

    Clone the repository:

    git clone https://github.com/LPavlovicCCT/capstone
    cd capstone

    Build and run the containers:
    This command will build the Django application image and start both the application and a PostgreSQL database container.

    docker-compose up --build

    The API will be available for testing at http://localhost:8000/api/nooks/

# CI/CD Pipeline

This project uses GitHub Actions for CI/CD, with workflows defined in .github/workflows/. The pipeline ensures that code is automatically tested and a new container image is built and published for every change merged to the main branch.

## Workflow Stages:

    Build and Push Workflow (test_views.yml): This workflow only when the there is a merge to the main branch.

    Build Image: If all tests pass, the workflow builds the Docker image for the application.

    Push to Registry: If the build is on the main branch, the new image is tagged and pushed to the GitHub Container Registry (ghcr.io), making it available for deployment.


# Kubernetes Deployment with Helm and Argo CD

The application is deployed to Kubernetes using a Helm chart and managed via a GitOps workflow with Argo CD.
## Prerequisites:

    A running Kubernetes cluster (k3d).

    kubectl configured to connect to your cluster.

    Helm CLI installed.

    Argo CD installed in the cluster.

## Deployment Steps:

The deployment is handled automatically by Argo CD. The Argo CD "Application" is configured to:

    Watch the Git Repository: It continuously monitors the main branch for changes.

    Use the Helm Chart: It uses the Helm chart located in the /book-catalog-chart directory as the source of truth for the application's desired state.

    Apply Overrides: It applies environment-specific values from the /enviroments/production/values.yaml file.

    Auto-Sync: When a new commit is pushed to main, Argo CD automatically syncs the changes, applying the new configuration to the cluster and creating a zero-downtime rolling update.
