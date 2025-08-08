Book Catalog API

This project is a RESTful API for managing a catalog of books, built with Django and deployed to a Kubernetes cluster using a fully automated CI/CD pipeline.
API Usage Examples

The API provides standard CRUD (Create, Read, Update, Delete) endpoints for managing books.
List All Books

curl CURL COMMAND HERE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

Create a New Book

curl CURL COMMAND HERE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

Retrieve a Specific Book

curl CURL COMMAND HERE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

Update a Book (Partial)

curl CURL COMMAND HERE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<</

Delete a Book

curl CURL COMMAND HERE<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

Local Development Setup
Prerequisites

    Docker

    Docker Compose

Running the Application

    Clone the repository:

    git clone https://github.com/LPavlovicCCT/capstone
    cd capstone

    Build and run the containers:
    This command will build the Django application image and start both the application and a PostgreSQL database container.

    docker-compose up --build

    The API will be available at http://localhost:8000/api/books/.

CI/CD Pipeline

This project uses GitHub Actions for continuous integration and continuous delivery. The workflows are in the .github/workflows/ directory.

    Test Workflow (test_views.yml): This workflow runs on every push and pull request. It installs dependencies and runs the Django unit tests to ensure code quality and correctness.

    Build and Push Workflow (test_views.yml): This workflow only when the there is a merge to the main branch.

        Build Image: It builds the Docker image for the application.

        Push to Registry: If the build is on the main branch, it pushes the image to the GitHub Container Registry (ghcr.io).

Kubernetes Deployment with Helm and Argo CD

The application is deployed to Kubernetes using a Helm chart and managed via a GitOps workflow with Argo CD.
Prerequisites:

    A running Kubernetes cluster (k3d).

    kubectl configured to connect to your cluster.

    Helm CLI installed.

    Argo CD installed in the cluster.

Deployment Steps

The deployment is handled automatically by Argo CD. The Argo CD "Application" is configured to:

    Watch the Git Repository: It continuously monitors the main branch for changes.

    Use the Helm Chart: It uses the Helm chart located in the /book-catalog-chart directory as the source of truth for the application's desired state.

    Apply Overrides: It applies environment-specific values from the /enviroments/production/values.yaml file.

    Auto-Sync: When a new commit is pushed to main, Argo CD automatically syncs the changes, applying the new configuration to the cluster and creating a zero-downtime rolling update.