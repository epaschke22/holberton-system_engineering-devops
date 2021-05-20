# fixes small misspelling in apache config
exec { 'modify_file':
    command => "sudo sed -i 's/phpp/php/g' /var/www/html/wp-settings.php"
}
