#!/bin/bash
set -e

sudo apt-get install -y git python-virtualenv
git clone https://github.com/ahussein/moboware_api.git -b development
sudo chown -R mobo:mobo moboware_api
cd moboware_api
./setup_env.sh
sudo cp config/webservice_uwsgi_upstart.config /etc/init.d/moboware_api.config
