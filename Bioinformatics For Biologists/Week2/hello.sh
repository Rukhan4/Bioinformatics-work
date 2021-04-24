#!/usr/bin/env bash

#Say hello
echo "Hello world!"

#Say my name GLOBALLY
export MY_NAME="Surur"
export GREETING="My name is:"
echo "${GREETING} ${MY_NAME}"

#Working with arrays
AGE_ARRAY=("20" "25" "30")
echo "I am ${AGE_ARRAY[0]} years old!"