### use instructions below
>sudo -s -H 

now you should enter root password (only once)

######install python
>add-apt-repository ppa:fkrull/deadsnakes

>apt-get update

>apt-get install python2.7

######install pip and virtualenv

>apt-get install python-setuptools

>easy_install pip

>pip install virtualenv

######install git

>apt-get update

>apt-get install git

>Y

######clone project and create virtualenv

>git clone https://github.com/nataliakushnir/secl.test.git

>cd secl.test

>virtualenv --no-site-packages .env

>source .env/bin/activate

######install mysql and mysql-server

>apt-get install python-dev

>Y

>apt-get install libmysqlclient-dev

>Y

>pip install mysql-python

>pip install mysqlclient

>apt-get install mysql-server

>Y

enter password

>admin

repeat password

>admin

>mysql -u root -p

>admin

>create database secl_task;

>exit;

>pip install -r requirements.txt

>python manage.py migrate

>python manage.py loaddata initial_data.json

>python manage.py runserver

open another terminal window to check functionality

>curl http://127.0.0.1:8000/

>curl http://127.0.0.1:8000/4?processed=true ...
