# Pyengine

## Prerequisite

Keyword | Value     | Description
----    | ----      | ----
PROJECT | catalog   | Project name
 
# Installation

## Install libraries

Pyengine is based on apache and python django framework

~~~bash
apt-get install -y python-dev python-pip mariadb-server apache2 libapache2-mod-wsgi python-mysqldb libyaml-cpp-dev libyaml-dev
~~~

## Install PIP libraries for django

~~~bash
pip install django
pip install django-log-request-id
pip install dicttoxml
pip install xmltodict
pip install routes
pip install rsa
pip install pytz
pip install pyyaml
~~~

## Download source

Download pyengine source

~~~bash
cd /opt/
git clone https://github.com/pyengine/catalog.git catalog
~~~

## Update python module path environment

edit /usr/local/lib/python2.7/site-packages/pyengine.pth

~~~text
/opt/catalog
~~~

# Update Configuration

## Update Apache configuration

edit /etc/apache2/conf-available/catalog.conf

~~~text
<VirtualHost *:80>
    Alias /static    /opt/catalog/static
    <Directory /opt/catalog/static>
        Require all granted
    </Directory>

    WSGIScriptAlias / /opt/catalog/pyengine/wsgi.py
    WSGIPassAuthorization On

    <Directory /opt/catalog/pyengine>
    <Files wsgi.py>
        Require all granted
    </Files>
    </Directory>

    AddDefaultCharset UTF-8
</VirtualHost>
~~~

Enable the pyengine

~~~bash
a2enconf catalog
~~~

# Create Database

Create pyengine database

~~~bash
mysql -u root -e "create database pyengine character set utf8 collate utf8_general_ci"
~~~

## Update django DB

~~~bash
mkdir /var/log/pyengine
chown -R www-data:www-data /var/log/pyengine

cd /opt/catalog
python manage.py makemigrations
python manage.py migrate
~~~

# Restart Apache

~~~bash
service apache2 restart
~~~

# Create Testing value

~~~python

import requests
import json
headers = {'content-type':'application/json'}

r = requests.post('http://127.0.0.1/catalog/v1/portfolios',headers=headers, data=json.dumps({'name':'Automation','owner':'Choonho Son'}))

result = json.loads(r.text)
print "Portpolio: http://${IP}/catalog/v1/portfolios/%s" % result['uuid']

r_data = {'portfolio_uuid': result['uuid'],
        'name':'Jeju',
        'short_description':'IT automation tool',
        'description':'Document based IT automation tool',
        'provided_by':'PyEngine',
        'vendor':'PyEngine'
        }

r = requests.post('http://127.0.0.1/catalog/v1/products',headers=headers,data=json.dumps(r_data))
result = json.loads(r.text)
print "Product: http://${IP}/catalog/v1/products/%s" % result['uuid']

r_data = {'email':'admin@example.com', 
            'support_link':'https://github.com/pyengine/catalog.git',
            'support_description': 'This is a service catalog system'
            }
r = requests.post('http://127.0.0.1/catalog/v1/%s/detail' % result['uuid'], headers=headers, data=json.dumps(r_data))
~~~
