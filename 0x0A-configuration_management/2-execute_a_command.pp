# kill a command

exec {'kill':
  command => 'pkill killmenow',
  }
