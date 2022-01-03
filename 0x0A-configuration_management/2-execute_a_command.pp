# executes a pkill command
exec { 'killmenow':
command  => 'pkill killmenow',
path     => 'usr/bin',
}
