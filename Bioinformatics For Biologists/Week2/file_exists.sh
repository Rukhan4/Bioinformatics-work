#!/usr/bin/env bash

#Create a function called file_exists taking the first argument (a filename) which it uses to see if the file exists. 
#If it doesn’t, return “File does not exist: “, followed by the filename.

function file_exists(){
    if [[ ! -e $1 ]]; then
        echo "File does not exist: $1"
    else
        echo "File exists: $1"
    fi
}

#Run function and specify where it receives argument from
file_exists "$1"