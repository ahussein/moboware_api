#!/bin/bash
set -e

sudo apt-get install -y git python-virtualenv
sudo git clone https://github.com/ahussein/moboware_api.git -b development
sudo chown -R mobo:mobo moboware_api
cd moboware_api
./setup_env.sh
sudo cp config/webservice_uwsgi_upstart.config /etc/init/moboware_api.conf
sudo cp config/webservice_nginx /etc/nginx/sites-available/moboware_api
sudo ln -s /etc/nginx/sites-available/moboware_api /etc/nginx/sites-enabled/

echo "Starting server"
sudo start moboware_api
