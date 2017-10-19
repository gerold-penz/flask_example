#############
Flask Example
#############


==============
Abhängigkeiten
==============

Damit man keine Abhängigkeiten auf dem Server installieren muss, werden diese im Ordner *lib* gleich mitgeliefert.
Alle Abhängigkeiten stehen in der Datei ``requirements.txt``. Diese werden mit ``python _update_requirements.py``
installiert und aktualisiert.

Dafür muss auf der Entwicklungs-Maschine **Pip** installiert sein. Unter Debian-Derivaten wird das mit
``sudo apt install python-pip`` installiert und einem anschließenden ``sudo pip install --upgrade pip`` auf den
aktuellsten Stand gebracht.


============
Installation
============

Ich habe mir in einer virtuellen Maschine einen Fedora-Server installiert um das ausprobieren zu können.

- Apache aktiviert und HTTP in der Firewall freigegeben (https://fedoraproject.org/wiki/Apache_HTTP_Server)

- Quellcode hochgeladen (https://github.com/gerold-penz/flask_example/) alles aus dem *application*-Ordner wurde in den
  *wsgi-anwendung*-Ordner kopiert.

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
            ├── Flask-0.12.2.dist-info
            └── ...

- */etc/httpd/conf.d/virualh.conf* erstellt::

    <VirtualHost *:80>
        ServerName fedora.local

        DocumentRoot /var/www/html

        <Directory /var/www/html>
            Order allow,deny
            Allow from all
        </Directory>

        WSGIScriptAlias / /var/www/wsgi-anwendung/anwendung.wsgi

    </VirtualHost>

Damit hat das dann schon funktioniert.

``DocumentRoot`` zeigt absichtlich nicht in den Ordner in dem sich die Anwendung befindet. So ist sichergestellt,
dass nicht von Aussen auf den Quellcode zugegriffen werden kann. Ansonsten kann man den Quellcode per *.htaccess*-Datei
absichern.

Eventuell benötigt das Programm noch ein paar Rechte im Dateisystem um Dateien zu erstellen.
Damit das funktioniert, sollte die WSGI-Anwendung als der Benutzer ausgeführt werden, mit dem man auch
die Dateien hochläd.

In diesem Fall muss man noch den Benutzer und die Gruppe in der Apache-Konfiguration mit übergeben.
Damit das funktioniert sieht die Apache-Konfiguration so aus::

    <VirtualHost *:80>
        ServerName fedora.local

        DocumentRoot /var/www/html

        <Directory /var/www/html>
            Order allow,deny
            Allow from all
        </Directory>

        # <UserName> und <GroupName> ersetzen
        WSGIDaemonProcess wsgi-anwendung user=<UserName> group=<GroupName>
        WSGIProcessGroup wsgi-anwendung
        WSGIScriptAlias / /var/www/wsgi-anwendung/anwendung.wsgi
        WSGIScriptReloading On

    </VirtualHost>

Mit ``WSGIScriptReloading On`` wird dem Apachen mitgeteilt, dass dieser das Programm beim nächsten Zugriff
neu startet, wenn sich die */var/www/wsgi-anwendung/application/anwendung.wsgi*-Datei ändert.


======
Testen
======

Wenn man SSH-Zugang zum Server hat, dann kann man die Anwendung direkt starten. Damit man dafür nicht extra
Flask installieren muss, habe ich ``_run_simple_wsgi_server.py`` geschrieben. Einfach mit ``python _run_simple_wsgi_server.py``
starten und schon kann man mit ``curl http://localhost:5000`` testen ob die Anwendung läuft. Läuft diese nicht,
wird sie erst gar nicht im Apachen laufen.
