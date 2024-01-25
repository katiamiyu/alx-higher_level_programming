#!/bin/bash
# this bash script outputs the size of the body of the response
curl -s $1 | wc -c 
