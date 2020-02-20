#Apache2 config
exec { 'Apache2 config':
  command  => 'sudo sed -i \'s/.phpp/.php/\' /var/www/html/wp-settings.php',
  provider => shell,
}
exec { 'Apach2 restart':
  command  => 'sudo service apache2 restart',
  provider => shell,
}
