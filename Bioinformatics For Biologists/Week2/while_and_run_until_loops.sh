#!/usr/bin/env bash

#Print 
#1
#2
#3

#METHOD 1 - WHILE LOOP
i=1 
while [[ $i -le 3 ]]
do
    echo "$i"
    ((i++))
done

printf "\n" # Space between methods
 

#METHOD 2 - UNTIL LOOP
a=1
until [[ $a -gt 3 ]]
do
    echo "$a"
    ((a++))
done