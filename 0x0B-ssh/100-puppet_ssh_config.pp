# edits a config file
file_line{'disable password login':
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}

file_line{'set ssh identity file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton'
}
