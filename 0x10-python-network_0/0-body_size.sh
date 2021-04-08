#!/bin/bash
# sends request to url to display size of body
curl $1 -s -w "%{size_download}\n" -o /dev/null
