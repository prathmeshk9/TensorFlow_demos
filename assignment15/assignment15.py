"""  
	get Requesting data
import requests
r = requests.get('http://coolacharya.com/connectory/events.json')
print r.content
"""


"""
	get Requesting data in json format
import requests
 
import requests
r = requests.get('https://api.github.com/events')
print r.json()
"""

""" 
	post requesting  data
from StringIO import StringIO
import requests
 
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print(r.text)

"""
""" header data in json format
#!/usr/bin/env python
import requests
r = requests.get('http://pythonspot.com/')
print r.headers

"""