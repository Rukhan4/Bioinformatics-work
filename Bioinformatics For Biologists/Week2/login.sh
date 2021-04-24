#!/usr/bin/env bash

#Get username
read -p "Enter your username: " username

#Get password
read -sp "Enter your password: " password

#Relay info

echo -e "\nHi ${username}, your password is ${password}"