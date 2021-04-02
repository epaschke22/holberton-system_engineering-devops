# kills a running programming
exec { 'kill':
  command => 'pkill killmenow'
  path    => '/bin/'
}
