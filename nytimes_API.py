#!/usr/bin/env python
# coding: utf-8

import requests
r = requests.get('https://api.nytimes.com/svc/community/v3/user-content/url.json?api-key=6xo5RmblUXnx5XIJaEgO03v7hpqfVI8O&offset=0&url=https%3A%2F%2Fwww.nytimes.com%2F2019%2F06%2F21%2Fscience%2Fgiant-squid-cephalopod-video.html')
r.json()

import json
var = json.loads(r.text) 

type(var)

var['results']['comments']

var['results']['comments'][0]['commentBody']

for element in var['results']['comments']:
    print (element['commentBody'])
