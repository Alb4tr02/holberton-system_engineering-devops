#change ULIMIT
exec { 'Change ULIMIT':
  command  => 'echo 'ULIMIT="-n 2500"' > /etc/default/nginx /etc/default/nginx && sudo service nginx restart',
  provider => shell,
}
