#!/bin/bash
curl -s -H "Content-Type: application/json" -d @"$2" "$1"
