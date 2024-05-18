#Enable the user holberton to login and open files without errors

# Increase hard file limit for holberton user
exec { 'increase-hard-file-limit-for-holberton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf'
  path    => '/usr/local/bin/:/bin/'
}

#Increase soft file limit for user holberton
exec { 'increase-soft-file-limit-for-holberton-user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf'
  path    => '/usr/local/bin/:/bin/'
}

file_line { 'pam_limits':
  path  => '/etc/pam.d/common-session',
  line  => 'session required pam_limits.so',
  match => '^#session required pam_limits.so',
}

file_line { 'pam_limits_noninteractive':
  path  => '/etc/pam.d/common-session-noninteractive',
  line  => 'session required pam_limits.so',
  match => '^#session required pam_limits.so',
}
