# Print Service (for GDCPC 2015)

## Dependencies

- python2, mysql, mysql-python, enscript (apt-get/yum/...)
- flask, flask-login, peewee, sh (pip install)

## Setup

### Configure
Copy `common/config.example.py` to `common/config.py` and edit it.
### Create database
`mysql> create database databasename;`
### Create user
`mysql> create user username@localhost identified by 'password';`
`mysql> grant all privileges on database.* to username@localhost;`
### Create table
`./createdb.py`
### Import User
`./importuser.py user.csv`

## Run

`./app.py`
