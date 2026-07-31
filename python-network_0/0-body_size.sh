#!/bin/bash
# Displays the size of the body of an HTTP response in bytes
curl -s "$1" | wc -c
