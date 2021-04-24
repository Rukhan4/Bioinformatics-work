#!/usr/bin/env bash

'''
Challenge
First, prompt the user to provide a cut and store their response in a variable called quality.

If the user enters either Fair or Good, return Insufficient quality to proceed.

If the user enters a value other than Premium, Ideal or Very Good, return Invalid cut.

Otherwise, count the number of diamonds (rows) which have the user-defined cut.
'''

read -p "Enter your cut:" quality

if [[ $quality == "Fair" ]] || [[ $quality == "Good" ]]

then

echo "Insufficient quality to proceed."

elif [[ $quality == "Premium" ]] || [[ $quality == "Ideal" ]] || [[ $quality == "Very Good" ]]

then

grep -c ${quality} Diamonds.csv

else

echo "Invalid cut"

fi