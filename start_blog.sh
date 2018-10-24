#!/usr/bin/bash

yum -y update
yum -y install yum-utils
yum -y groupinstall development


# install python
yum -y install https://centos7.iuscommunity.org/ius-release.rpm
yum -y install python36u
yum -y install python36u-pip
yum -y install python36u-devel
ln -s /usr/bin/python3.6 /usr/bin/python3
ln -s /usr/bin/pip3.6 /usr/bin/pip3
pip3 install --upgrade pip
pip3 install django
pip3 install uwsgi

# install nginx 
cat << EOF > /etc/yum.repos.d/nginx.repo
[nginx]
name=nginx repo
baseurl=http://nginx.org/packages/centos/7/\$basearch/
gpgcheck=0
enabled=1
EOF

yum install -y nginx

mv /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf_backup
cat << EOF > /etc/nginx/conf.d/mysite.conf

# the upstream component nginx needs to connect to
upstream django {
    # server unix:///path/to/your/mysite/mysite.sock; # for a file socket
    server 127.0.0.1:8001; # for a web port socket (we'll use this first)
}

# configuration of the server
server {
    # the port your site will be served on
    listen      80;
    # the domain name it will serve for
    server_name $1; # substitute your machine's IP address or FQDN
    access_log  /var/log/nginx/access.log;
    error_log   /var/log/nginx/error.log;
    charset     utf-8;
    gzip on;
    gzip_types text/plain application/x-javascript text/css text/javascript application/x-httpd-php application/json text/json image/jpeg image/gif image/png application/octet-stream;

    error_page  404           /404.html; 
    error_page   500 502 503 504  /50x.html;

    # max upload size
    client_max_body_size 75M;   # adjust to taste

    # Django media
    location /media/ {
        alias /root/code/django_blog/media/;  # your Django project's media files - amend as required
    }

    location /static/ {
        alias /root/code/django_blog/static/;
    }

    # Finally, send all non-media requests to the Django server.
    location / {
        include uwsgi_params;
        uwsgi_connect_timeout 30;
        uwsgi_pass unix:/root/code/django_blog/uwsgi.sock;
    }
}
EOF


# download django blog 
mkdir -p /root/code/
cd /root/code/
git clone https://github.com/otfsenter/django_blog.git
cd /root/code/django_blog
touch  uwsgi.log 

chmod +x -R /root/code


echo "collectstatic and create superuser"
echo "nginx server name"
echo "then start uwsgi and nginx"




