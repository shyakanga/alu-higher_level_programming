#!/bin/bash
# Sends a JSON POST request with contents of a file passed as second argument
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
