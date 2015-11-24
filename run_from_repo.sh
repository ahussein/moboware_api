#!/bin/bash
set -e

# Install the required software on the ubuntu system
# we need to install git and python-virtualenv
# git will be used to clone the repository that contain the code for the API and python-virtualenv will
# be used to create a container runtime environment for the python process
sudo apt-get install -y git python-virtualenv
cd /opt/

# clone the repository (development branch)
# todo: think about creating a package for the python package and how to distribute it
sudo git clone https://github.com/ahussein/moboware_api.git -b development

# make sure to change ownership for the newly cloned repository directory
# todo: allow the user to be configured, maybe provided to the script
sudo chown -R mobo:mobo moboware_api
cd moboware_api

# call the setup env shell script to configure and install the required dependencies
./setup_env.sh

# copy the configurations files from the repository directory to the actual system directory
# the following file is the upstart configuration file to make that the moboware_api service is started automatically
# on system boot up
sudo cp config/webservice_uwsgi_upstart.config /etc/init/moboware_api.conf

# nginx configuration file for serving using uwsgi gateway to execute the python program
sudo cp config/webservice_nginx /etc/nginx/sites-available/moboware_api
sudo ln -s /etc/nginx/sites-available/moboware_api /etc/nginx/sites-enabled/

# make sure to remove the default nginx configurations
sudo rm /etc/nginx/sites-enabled/default

# make sure that the log directory for uwsgi startup is created
mkdir -p logs/uwsgi

echo "Starting server"
sudo restart moboware_api

sudo restart nginx
