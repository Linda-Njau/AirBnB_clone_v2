#!/usr/bin/env bash
#this script sets up web servers for deployment

sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
sudo echo "This page is just for gigs" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
