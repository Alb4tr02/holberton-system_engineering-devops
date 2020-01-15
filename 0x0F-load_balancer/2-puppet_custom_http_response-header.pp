#config server

exec {'add_header':

command => '/usr/bin/sudo /bin/sed -i "60i add_header X-Served-By \$hostname;" /etc/nginx/nginx.conf',
}
exec {'start_server':

command => '/usr/bin/sudo /usr/sbin/service nginx start',
}
