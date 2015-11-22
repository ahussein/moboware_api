#!/bin/bash
set -e

sudo apt-get update
sudo apt-get install -y build-essential python-dev python-pip nginx
rm -rf venv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt

echo "Initialize server"
python manage.py -i
