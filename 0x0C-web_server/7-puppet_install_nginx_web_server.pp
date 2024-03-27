mode default{
package { 'nginx':
ensure => 'installed',
}

file {'/var/www/html':
content => 'Hello World!'
mode => '0644',
}

}
