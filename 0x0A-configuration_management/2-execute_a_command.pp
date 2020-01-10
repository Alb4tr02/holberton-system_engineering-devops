# kill a command

exec {'kill':
  command => '/usr/bin/pkill killmenow',
  }
