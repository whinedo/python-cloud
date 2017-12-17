#!/bin/bash


curl -i -H "Content-Type: application/json" -X POST -d '{"username":"mahesh@rocks", "email": "mahesh99@gmail.com","password": "mahesh123", "name":"Mahesh" }' http://localhost:5000/api/v1/users

curl -i -H "Content-Type: application/json" -X delete -d '{ "username":"manish123" }' http://localhost:5000/api/v1/users

curl -i -H "Content-Type: application/json" -X POST -d '{"username":"mahesh@rocks","body": "It works" }' http://localhost:5000/api/v2/tweets

curl http://localhost:5000/api/v2/tweets -v

curl http://localhost:5000/api/v2/tweets/1

nosetests-3.4 -v --with-coverage flask_test.py