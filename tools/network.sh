#!/bin/bash

hour=$(date +%H | sed 's/^0//')

if ((hour >= 4 && hour < 12)); then
    echo "Good morning, Ansah"
elif ((hour >= 12 && hour < 17)); then
    echo "Good afternoon, Ansah"
else
    echo "Good evening, Ansah"
fi

sleep 0.5
echo "restarting the Network"
sudo systemctl restart NetworkManager

if ping -c 5 172.16.1.1; then
    echo "Network connected, LOGIN"
    # loading env variable
    source env/bin/activate
    sleep 0.5
    export username=U21CS070
    export password=U21CS070

    echo "Initiating Login Process"
    python3 wiJungle.py
else
    echo "Not connected"
    echo "Wanna retry? (y/n)"
    read val
    if [[ "$val" == 'y' ]]; then
        ./network.sh
    fi
fi
