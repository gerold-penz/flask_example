#############
Flask Example
#############

Servus Hannes!

Ich habe mir in einer virtuellen Maschine ein Fedora installiert um testen zu können.

Apache aktiviert

HTTP in der Firewall freigegeben

Quellcode hochgeladen (siehe : https://github.com/gerold-penz/flask_example/)

::

    /var/www/
    ├── cgi-bin
    ├── html
    ├── usage
    └── wsgi-anwendung
        ├── http_root
        │   └── testpage
        └── lib
            ├── click
            ├── click-6.7.dist-info
            ├── flask
            │   └── ext
            ├── Flask-0.12.2.dist-info
            ├── itsdangerous-0.24.dist-info
            ├── jinja2
            ├── Jinja2-2.9.6.dist-info
            ├── markupsafe
            ├── MarkupSafe-1.0.dist-info
            ├── werkzeug
            │   ├── contrib
            │   └── debug
            │       └── shared
            └── Werkzeug-0.12.2.dist-info

*/etc/httpd/conf.d/viruald.conf* erstellt::

    <VirtualHost *:80>
        ServerName fedora.local

        DocumentRoot /var/www/html

        <Directory /var/www/html>
            Order allow,deny
            Allow from all
        </Directory>

        WSGIScriptAlias / /var/www/wsgi-anwendung/application/anwendung.wsgi

    </VirtualHost>

Eventuell benötigt das Programm noch ein paar Rechte im Dateisystem um Dateien zu erstellen.
Damit das funktioniert, sollte die WSGI-Anwendung als der Benutzer ausgeführt werden, mit dem man auch
die Dateien hochläd.
In diesem Fall muss man noch den Benutzer und die Gruppe in der Apache-Konfiguration mit übergeben.
Damit das funktioniert sieht die Apache-Konfiguration so aus (Benutzer und Gruppe: *gerold*)::

    <VirtualHost *:80>
        ServerName fedora.local

        DocumentRoot /var/www/html

        <Directory /var/www/html>
            Order allow,deny
            Allow from all
        </Directory>

        WSGIDaemonProcess wsgi-anwendung user=gerold group=gerold
        WSGIProcessGroup wsgi-anwendung
        WSGIScriptAlias / /var/www/wsgi-anwendung/application/anwendung.wsgi
        WSGIScriptReloading On

    </VirtualHost>

Mit ``WSGIScriptReloading On`` wird dem Apachen mitgeteilt, dass dieser das Programm beim nächsten Zugriff
neu startet, wenn sich die */var/www/wsgi-anwendung/application/anwendung.wsgi*-Datei ändert.


