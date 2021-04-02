# kills a running programming
exec { 'kill':
  command => 'pkill killmenow',
  path    => '/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
}
