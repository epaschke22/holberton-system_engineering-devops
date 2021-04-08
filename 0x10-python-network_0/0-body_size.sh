#!/usr/bin/env bash
# sends request to url to display size of body
curl $1 -w "%{size_download}\n" -o /dev/null -s
