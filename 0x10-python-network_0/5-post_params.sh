#!/bin/bash
# a Bash script takes in a URL, sends a POST request to the supplied URL
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" -X POST $1
