#!/usr/bin/python

import json

hosts = '10.10.10.247';
print json.dumps({'all': hosts, '_meta': {'hostvars': {}}})
