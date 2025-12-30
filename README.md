# End to End Machine Learning Project

#Deployment-Run from terminal
#Container Registry URL: testdockerdeploy.azurecr.io
docker build -t testdockerdeploy.azurecr.io/studentperformance:latest .
docker login testdockerdeploy.azurecr.io
docker push testdockerdeploy.azurecr.io/studentperformance:latest
