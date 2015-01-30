#!/usr/bin/env python

import urllib2
import json
import MySQLdb

ip='42.121.143.104'
response = urllib2.urlopen('http://freegeoip.net/json/' + ip)
#print 'RESPONSE:', response
#print 'URL     :', response.geturl()
data = response.read()
print data
loc=json.loads(data)
print loc['country_name']


db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="abc123", # your password
                      db="fafa", unix_socket="/opt/lampp/var/mysql/mysql.sock") # name of the data base

cur = db.cursor() 
cur.execute("SELECT * FROM member limit 20" )
for row in cur.fetchall() :
    print row[0]