#!/usr/bin/env bash
#this script sets up web servers for deployment

if ! command -v nginx &> /dev/null
then
    sudo apt-get update
    sudo apt-get install -y nginx
fi
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p data/web_static/shared/
sudo chown -R ubuntu:ubuntu /data/
echo "<html><head><title>Test</title></head><body>This is a test page</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null
sudo rm -rf /data/web_static/current
sudp ln -s /data/web_static/releases/test/ /data/web_static/current
sudo sed -i '/server_name localhost;/ a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
