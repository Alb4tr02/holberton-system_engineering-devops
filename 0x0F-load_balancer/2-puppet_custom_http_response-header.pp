#config server
exec {'update':
command => '/usr/bin/sudo /usr/bin/apt-get  -y update',
}

exec {'install':
command => '/usr/bin/sudo /usr/bin/apt-get  -y install nginx',
}

exec {'hlbtn_page':
command => '/usr/bin/sudo /bin/echo Holberton School > /var/www/html/index.nginx-debian.html',
}
exec {'redirect_page':

command => '/usr/bin/sudo /bin/sed -i "66i rewrite ^/redirect_me https://www.youtube.com/ permanent;" /etc/nginx/sites-available/default',
}
exec {'add_header':

command => '/usr/bin/sudo /bin/sed -i "60i add_header X-Served-By \$hostname;" /etc/nginx/nginx.conf',
}
exec {'start_server':

command => '/usr/bin/sudo /usr/sbin/service nginx start',
}
