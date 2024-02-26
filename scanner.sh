#!/bin/bash

subnet=$1

if [ -z "$subnet" ]; then
    echo "Usage: $0 <SUBNET>"
    exit 1
fi

for addr in $(seq 1 254); do
    ip="${subnet}.${addr}"
    if ping -c 1 -W 1 "$ip" &> /dev/null; then
        if nc -zvw1 "$ip" 1-65535 &> /dev/null; then
            echo "Host $ip is up, with open ports:"
            nc -zvw1 "$ip" 1-65535 2>&1 | grep succeeded
        else
            echo "Host $ip is up, but no open ports found."
        fi
        else
                 echo "Host $ip is down."
    fi
done

