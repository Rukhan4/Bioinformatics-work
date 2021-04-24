#!/usr/bin/env bash

#Store command line argument in variable called animal
ANIMAL="$1"

#Use CASE SWITCH statements with the following conditions and responses:
# When the user enters cow, return “Here, moo”
# When the user enters sheep, return “There a baa”
# When the user enters duck, return “Everywhere a quack”
# Otherwise, return “Old MacDonald had a farm”

case $ANIMAL in
    cow)
    echo "Moo"
    ;;
    sheep)
    echo "Baa"
    ;;
    duck)
    echo "Quack"
    ;;
    *)
    echo "The Farmhouse"
    ;;
esac