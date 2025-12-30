
# Student Performance ML Project

End-to-end machine learning project for student performance prediction, containerized with Docker and deployed to Azure Container Registry.

## Installation

Ensure Docker is installed, then build and run locally:

Build the Docker image
```docker build -t testdockerdeploy.azurecr.io/studentperformance:latest .```

Run locally to test
```docker run -p 8000:80 testdockerdeploy.azurecr.io/studentperformance:latest```


## Deployment to Azure Container Registry

Login to ACR
```docker login testdockerdeploy.azurecr.io```

Push to ACR
```docker push testdockerdeploy.azurecr.io/studentperformance:latest```


**Container Registry:** `testdockerdeploy.azurecr.io`
