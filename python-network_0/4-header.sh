#!/bin/bash
# Sends a GET request to the URL passed as argument with a custom header
curl -s -H "X-School-User-Id: 98" "$1"
