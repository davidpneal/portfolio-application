# portfolio-application

## Overview

This project is designed to be a demonstration of a simple CRUD application running in an environment provisioned via Infrastructure as Code.  This application will be tied into a CI\CD pipeline to handle deployments to prod and the other environments.  The goal is to automate as much of this process as possible.  

This is the application repository which hosts a simple "Fortune of the day" type website which users can interact with and perform simple database lookups and additions through the web interface.


## Pre-requisites

The website is written with a Python framework called Flask.  This site was built using Python 3.7.1 along with the following packages.

These packages can be installed via pip:
* Flask
* Flask-WTF, installing this will also automatically install the WTForms package
* Flask-sqlalchemy, this will also install SQLAlchemy automatically


## Running the website

This application is still under development but can easily be launched on the local workstation in a dev webserver that Flask helpfully provides.  It can be launched by navigating to the folder containing the package and running `python run.py`

The site will be available at `http://localhost:5000`
