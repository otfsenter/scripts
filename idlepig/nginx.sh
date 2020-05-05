#!/usr/bin/bash

docker rm -f idle


docker run --name idle -p 80:80 -v /root/html/otfsenter.github.io:/usr/share/nginx/html --restart=always -d nginx 
