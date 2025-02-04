# Deploy Web App Container in Azure Container App using GitHub Actions 🚀

![Activity Diagram](./assets/DeployApponAzure.png)

This GitHub Action automates the deployment of a web application container to an Azure Container App.

## Prerequisites

Before using this workflow, ensure you have:

- An Azure Container Registry (ACR) and an Azure Container App set up.
- The necessary secrets should created & stored in your GitHub repository under **Settings > Secrets and variables > Actions**:

| Secret Name            | Description                            |
|------------------------|----------------------------------------|
| AZURE_REGISTRY_USERNAME | Azure Container Registry username      |
| AZURE_REGISTRY_PASSWORD | Azure Container Registry password      |
| AZURE_CLIENT_ID         | Azure service principal client ID      |
| AZURE_CLIENT_SECRET     | Azure service principal client secret  |
| AZURE_TENANT_ID         | Azure tenant ID                        |
| AZURE_SUBSCRIPTION_ID   | Azure subscription ID                  |

## How Flow Works

This GitHub Action workflow consists of two main jobs:

### 1. Push Docker Image to Azure Container Registry (ACR) [CI]

- **Check out the repository**: Pull the latest code from the repository.
- **Log in to ACR**: Use `docker/login-action` to authenticate to your Azure Container Registry.
- **Set a short SHA for versioning**: Generate a short SHA hash of the commit to use as a version tag for the Docker image.
- **Build the Docker image**: Use `docker/build-push-action` to build the Docker image based on your Dockerfile.
- **Push the image to ACR**: Push the Docker image to your Azure Container Registry.

### 2. Deploy to Azure Container Apps [CD]

- **Log in to Azure**: Use `azure/login` to authenticate to your Azure account.
- **Deploy the container to Azure Container Apps**: Use `azure/container-apps-deploy-action` to deploy the Docker container to Azure Container Apps.

## How to Create Resources in CLI

To set up the required Azure resources, you can use the following Azure CLI commands:

### 1. Create Resource Group
```bash
az group create --name irusha-rg --location eastus
```

### 2. Create Azure Container Registry (ACR)
```bash
az acr create --name irusha --resource-group irusha-rg --sku Basic
```

### 3. Create Azure Container App
```bash
az containerapp create \
  --name mywebapp \
  --resource-group irusha-rg \
  --image irusha.azurecr.io/mywebapp:latest \
  --target-port 80 \
  --cpu 1 --memory 1.5Gi
```

### 4. Set up a Service Principal for Azure Authentication
```bash
az ad sp create-for-rbac --name "github-actions" --role contributor --scopes /subscriptions/<subscription-id>/resourceGroups/irusha-rg
```

## How to Run

### 1. Configure Secrets

Ensure all required secrets are added to your GitHub repository under **Settings > Secrets and variables > Actions**.

### 2. Modify Environment Variables (If Needed)

Update the following environment variables in `.github/workflows/deploy.yml` as needed:
```yaml
env:
  AZURE_CONTAINER_REGISTRY: irusha.azurecr.io
  CONTAINER_APP_NAME: mywebapp
  RESOURCE_GROUP: irusha
```

## How to Run

### 3. Trigger the Workflow

Push any code changes to the repository, and GitHub Actions will automatically build, push, and deploy the container.

### 4. Verify Deployment

After deployment, verify the running container in the Azure Portal:
- Navigate to **Azure Portal**.
- Go to **Container Apps**.
- Select your container app and check the running container.
- Access the application using the provided URL.

## Notes

- Ensure your Azure credentials and permissions are correctly configured for deployment.
- The **SHORT_SHA** is used to uniquely tag Docker images per commit.
- Modify the Dockerfile in the repository to define how the container should be built.

## Troubleshooting

### Issue: Authentication Issues
**Solution**: Verify that all required secrets are correctly set up.

### Issue: Deployment Failures
**Solution**: Check GitHub Actions logs for errors.

### Author Information

**Author**: Irusha Malalgoda  
**Date**: 4th February 2025  
**GitHub**: [github.com/irushahm](https://github.com/irushahm)
**LinkedIn**: [linkedin.com/in/ihasantha](https://linkedin.com/in/ihasantha)
