#!/bin/bash

while true; do
    echo -n "duck "
    random_num=$((RANDOM%6))
    if [ "$random_num" -eq 0 ]; then
        echo "goose!"
        break
    fi
done

