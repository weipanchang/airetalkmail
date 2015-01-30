#!/usr/bin/env python

import urllib2

response = urllib2.urlopen('http://freegeoip.net/json/42.121.143.104')
print 'RESPONSE:', response
print 'URL     :', response.geturl()
data = response.read()
print data
