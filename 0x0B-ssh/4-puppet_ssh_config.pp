# edits a config file
file_line{'disable password login':
  ensure => 'absent'
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication yes',
}

file_line{'set ssh identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton'
}
