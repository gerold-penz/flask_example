#############
Flask Example
#############

====================
Apache Konfiguration
====================


::

    <VirtualHost *:80>

        ServerName www.example.com
        ServerAlias example.com
        ServerAdmin webmaster@example.com

        DocumentRoot /usr/local/www/documents

        <Directory /usr/local/www/documents>
            Order allow,deny
            Allow from all
        </Directory>

        WSGIScriptAlias /myapp /usr/local/www/wsgi-scripts/myapp.wsgi

        <Directory /usr/local/www/wsgi-scripts>
            Order allow,deny
            Allow from all
        </Directory>

    </VirtualHost>
