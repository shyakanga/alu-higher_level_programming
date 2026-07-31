#!/bin/bash
# Sends a POST request with parameters email and subject
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
