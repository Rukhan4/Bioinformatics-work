#!/usr/bin/env bash

#1 Read a command line argument into a variable called temperature
TEMPERATURE="$1"
#echo "${temperature}"

#2 Create min 10 variable
MIN=10
#echo "${min}"

#3 Create max 30 variable
MAX=30

#CONDITIONS: 
#1) Return "Too hot!" if Temperature > max
#2) Return "Too cold!" if Temperature < min
#3) Return "Just right!" if Temperature <= max AND Temperature >= min

if [[ TEMPERATURE -gt MAX ]]; then
    echo "Too hot!"
elif [[ TEMPERATURE -lt MIX ]]; then
    echo "Too cold!"
else echo "Just right!"
fi

#BROKEN DOWN 

#1)

# if [[ TEMPERATURE -gt MAX ]]; then
#     echo "Too hot!"
#fi

#2)

# if [[ TEMPERATURE -lt MIN ]]; then
#     echo "Too cold!"
#fi


#3) 

# if [[ TEMPERATURE -ge MIN ]] && [[ TEMPERATURE -le MAX ]]; then
#     echo "Just right"
#fi

