# 0x19. Postmortem
https://intranet.hbtn.io/projects/294


# Issue Summary:

An Apache server running on a LAMP stack was returning a 500 error when receiving GET request. The website only contains 1 HTML page so the problem with MySQL or PHP was likely. 

## Timeline

- 5/18/21 - 1:31pm :  curling the website, WordPress returned a 500 error
- 5/18/21 - 1:32pm :  check all process running with `ps auxf`. This showed Apache and MySQL were running fine, which points to PHP/WordPress. 
- 5/18/21 - 1:34pm : The WordPress config file in `/var/www/html/wp-config.php` was edited recently.
- 5/18/21 - 1:37pm : Typographical error was found in config file which miss typed `.php` as `.phpp`
- 5/18/21 - 1:38pm : Manual restart after typo fix returns a 200 status.
- 5/18/21 - 1:42pm : Puppet script is created to implement fix for other servers.

## Root Cause

A typographical error in the WordPress config file on like 137.
`require_once( ABSPATH . WPINC . ‘/class-wp-locale.phpp’ );`
File extension should have read `.php`.

## Solution

After fixing the error manually, a puppet script is created to be run on all servers to fix the error.
This is the code used:
`exec { 'modify_file':
command => "sudo sed -i 's/phpp/php/g' '/var/www/html/wp-settings.php'",
path => '/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'}`

## Prevention

All servers should have error logging turned on to easily identify problems when they arise.
The user that updated the config file should have ran a test to see if their change still functioned.
Code should never be deployed to all servers before testing.
