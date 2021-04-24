#!/usr/bin/env bash

 
#Create a for loop which iterates from 1 to 5 in increments of 1. If the value is 2 return “fizz” otherwise, return “buzz”.


for ((i=1; i<=5; i++))
do
    if [[ ${i} == "2" ]]; then #can use -eq instead of == to symbolize equality
        echo "Fizz"
    else
        echo "Buzz"
fi
done