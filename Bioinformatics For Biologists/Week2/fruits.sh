#!/usr/bin/env bash

array=("pineapple" "peach" "raspberry" "plum" "apple" "kiwi")

#Output no. elements and last element
echo "Number of fruits: ${#array[@]}"

#Output last element of array
 echo "Last element: ${array[-1]}"
