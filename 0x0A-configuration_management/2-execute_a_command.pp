exec { 'kill':
  command => 'pkill killmenow'
  path => '/bin/'
}
