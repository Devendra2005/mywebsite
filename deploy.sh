#!/bin/bash
cd /var/www/mywebsite || exit
git pull origin main
sudo systemctl reload nginx

