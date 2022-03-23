#!/usr/bin/python

import json

host_list = ['10.10.10.140'.format(i) for i in range(11)]

r = {'_meta': {'hostvars': {}}, 'all': {'hosts': host_list}}

json.dumps(r)
