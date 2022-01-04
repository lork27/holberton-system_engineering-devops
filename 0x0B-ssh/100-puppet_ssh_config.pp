# puppet which appends two lines to ssh_config to change server behaviour
include stdlib
file { '/etc/ssh/ssh_config':
  ensure => present
}
-> file_line { 'IdentityFile':
  line => 'IdentityFile ~/.ssh/school',
  path => '/etc/ssh/ssh_config',
}
-> file_line { 'passline':
  line => 'PasswordAuthentication no',
  path => '/etc/ssh/ssh_config',
}
