# Copyright (c) 2025 sakib-maho
# Licensed under the MIT License
# See LICENSE file for details

from html.parser import HTMLParser
import urllib.request
from pprint import pprint
from itertools import count
import os
import json
import shelve
from contextlib import contextmanager

url = 'https://www.vrbo.com/vacation-rentals/condos-and-apartments/usa/florida/north-west/panama-city-beach'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozila'})

with urllib.request.urlopen(req) as html:
  page = html.read()