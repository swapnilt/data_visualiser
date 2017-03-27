# Weather data visualiser
## Requirements
*  Python 2.7
*  Redis 3.2.8
* PostgreSQL 9.4

To run on localhost, 
create database `kisanhub`


    git clone https://github.com/swapnilt/data_visualiser    
    cd data_visualiser    
    virtualenv env    
    source env/bin/activate    
    pip install -r requirements.txt

update database credentials in `data_visualiser/settings.py`.

Make sure redis can accept connection on unix socket and the socket name is updated in `data_visualiser/settings.py`


    python manage.py migrate    
    python manage.py runserver

Also, make sure you're running rqworker with,

    python manage.py rqworker default
    
