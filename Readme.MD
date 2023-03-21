This is a product API that enables you to

- see list of product
- detail of a product
- update a product
- delete a product

It uses MYSQL for the database service to work with it you need to create a user in my sql

- first login your root user
- second `mysql -u root -p`  add your password once asked
- Create new database `CREATE DATABASE Test;`
- Create the user for that database `CREATE USER 'username'@'hostname' IDENTIFIED BY 'password';`
- Grant the user access to the database `GRANT ALL PRIVILEGES ON Test.* TO 'username'@'hostname';`
- Alter role
    - `ALTER USER 'username'@'hostname' IDENTIFIED WITH mysql_native_password BY 'password';`
    - `ALTER USER 'username'@'hostname' DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;`
    - `SET TRANSACTION ISOLATION LEVEL READ COMMITTED;`
    - `SET time_zone = '+00:00';`

### Set Project Up

### Activation Virtualenv

- `pip install virtualenv `
- `virtualenv venv`

if you are using windows

- `venv\Scripts\activate.bat`

else

- `source env/bin/activate`

installing packages ( make sure you are in the root folder)

- `pip install -r requirements.txt`