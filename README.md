# EpicMail-Api

[![Coverage Status](https://coveralls.io/repos/github/Emmanuelaaron/EpicMail-Api/badge.svg?branch=develop)](https://coveralls.io/github/Emmanuelaaron/EpicMail-Api?branch=develop)


## Getting started
You can clone this [repo](https://github.com/Emmanuelaaron/EpicMail-Api.git) on your local machine or checkout the user-interface on [gh-pages](https://emmanuelaaron.github.io/EpicMail/UI/temps/signin.html).
### Prerequisites
Install [python](https://www.python.org/downloads/release/python-371/) on your local machine

### Installing
Clone the this repo on your local machine
```
$ git clone https://github.com/Emmanuelaaron/EpicMail-Api.git
```
cd into the cloned directory, install the virtual environment and activate it, checkout to the most stable branch and install all the dependences.
```
$ cd develop
$ pip install virtualenv
$ virtualenv venv
$ source venv/Scripts/activate
$ git checkout develop
$ pip install flask
$ pip install PyJWT
$ pip install -r requirements.txt
$ python run.py
```
* copy the Url it into postman and put to run any endpoint of your preference in the table below with the url prefix ('/api/v2') for each endpoint.

HTTP Method | Endpoint | Functionality | Parameters 
------------|----------|---------------|------------
POST | /auth/signup | User is able to signup | None
POST | /auth/login | User is able to login | None
POST | /messages | Creates a message| None
GET | /messages| Gets all received messages| None
GET | /messages/sent | Gets all sent messages | None
GET | /messages/<int:message_id> | Gets a specific message | message_id 
DELETE | /messages/<int:message_id> | deletes a specific message | message_id

## Running Tests
Install pytest, activate the virtual environment and then run the tests
```
$ pip install pytest
$ pytest
```
You can checkout the code coverage by using the code below
```
$ pytest --cov=.
```
Make sure your virtual environment is activated


## Tools Used
* [python](https://www.python.org/downloads/release/python-371/)
* [Flask](http://flask.pocoo.org/) Micro web framework for python
* [pip](https://pip.pypa.io/en/stable/) package installer for python
* [Virtualenv](https://virtualenv.pypa.io/en/stable/) Tool used to created isolated programs for python

## Built with
So far this application has been built with
* [Python](https://www.python.org/downloads/release/python-371/)
* [Flask](http://flask.pocoo.org/)


## Contributions
To contribute to this project please create a branch off the develop after which you will create a pull request before it is merged back.

## Aurthor
By Emmanuel Isabirye
