# Elections-Tallying-System(UCHAGUZI APP)
# NATION DECIDES
NAtion Decides is a web application that allows users to easily access the results of an election when the presiding officer posts the results. A user just loads the system and the results will be dynamically updated when every presiding officer posts there respective constituency results. 
***
## TABLE OF CONTENTS
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Requirements](#requirements)
- [Installation Guide](#installation-guide)
***
## Technologies Used
- Python 3.10
- Django 4
- Sqlite Database
- Html/Css/Bootstrap
***
## Features

***
## Requirements
To run this application, the user needs to have python3 installed in their system. They can download it [here](https://www.python.org/downloads/release/python-3108/).
***
## Installation Guide
To run this application, you first need to create a directory:
```bash
mkdir 'your directory'
```
Enter your directory and create a virtual environment:
```bash
pip install virtualenv
python3.10 -m venv env
```
Activate the virtual environment:
```bash
source env\bin\activate
```
clone the repository
```bash
git clone https://github.com/evanskiprotich/Elections-Tallying-System.git
```
Install the requirements
```bash
pip install -r requirements.txt
```
Enter the directory
```bash
cd Election-Tallying-System
```
Inside settings.py scroll down to the bottom and install the Email settings with yours.
Make migrations with this command in the terminal
```bash
python manage.py makemigrations
python manage.py migrate
```
Create a superuser running this command in the terminal
```bash
python manage.py createsuperuser
```
Run the app
```bash
python manage.py runserver
```