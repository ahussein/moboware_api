#!/bin/bash
set -e

sudo apt-get install -y git python-virtualenv
git clone https://github.com/ahussein/moboware_api.git -b development
cd moboware_api
./setup_env.sh
