#!/bin/bash

for letter in {A..Z} {a..z}; do

    response=$(curl -X POST -H "Host: ctfvol2.thm" -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/109.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8" -H "Accept-Language: en-US,en;q=0.5" -H "Accept-Encoding: gzip, deflate" -H "Content-Type: application/x-www-form-urlencoded" -H "Origin: http://ctfvol2.thm" -H "Referer: http://ctfvol2.thm/game1/" -H "Cookie: Invited=0" -H "Upgrade-Insecure-Requests: 1" --data "answer=$letter" --compressed --silent http://ctfvol2.thm/game1/)

    hash=$(echo "$response" | grep -oP '<p>Your hash:\s+\K\d+')

    echo "$letter : $hash"

done