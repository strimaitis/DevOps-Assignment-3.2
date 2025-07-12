# Assignment 3.2

This app is to be run in a Jenkins container with the following instructions in order to fufill the assignment's requirments.  Additional instructions on setting up a Jenkins image and running the container can be found [here](https://www.jenkins.io/doc/book/installing/docker/).

## Setup

Create a new pipeline item with the following specifications

1.) **General**:

Select the box for Github project and set the project file to "https://github.com/strimaitis/DevOps-Assignment-3.2.git/"

2.) **Triggers**: 

Select Poll SCM box and set schedule to "* * * * *".  This will poll the repository every minute and run a build when the project changes from a new commit merged directly into main.

3.) **Pipeline**:

a.) Select from dropdown "Pipeline script from SCM"

b.) Set Repository URL to "https://github.com/strimaitis/DevOps-Assignment-3.2.git/"

c.) Set branch to build to "*/main"

d.) Set script path to "Jenkinsfile"

## Build

To run the web application run a manual build or update the app with a commit. Once building the Jenkinsfile will install the frameworks in requirements and commence testing.

## Test

The application will run the over five unit tests written using Pytest framework and run a general lint test using Pylint. After the build is completed inspect it and open the console to view the results. As a rule of thumb the build will fail in Jenkins if the unit tests are changed such that any fail/

