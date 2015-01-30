#!/usr/bin/env python

import urllib2
import json
import MySQLdb

#ip='42.121.143.104'
#response = urllib2.urlopen('http://freegeoip.net/json/' + ip)
##print 'RESPONSE:', response
##print 'URL     :', response.geturl()
#data = response.read()
#print data
#loc=json.loads(data)
#print loc['country_name']
country=[]

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="abc123", # your password
                      db="fafa", unix_socket="/opt/lampp/var/mysql/mysql.sock") # name of the data base

cur = db.cursor() 
cur.execute("SELECT * FROM member limit 20" )
for row in cur.fetchall() :
    #print row[0], row[1], " ", row[2], " ",row[3], " ",row[4], " ",row[5], " ",row[6], " ",row[7] ,row[8], " ",row[9],row[10], " ",row[11], "\n"
    #print row[3], " ", row[5]," ",row[11], "\n"
    ip =row[11]
    response = urllib2.urlopen('http://freegeoip.net/json/' + ip)
    data = response.read()
    loc=json.loads(data)
    if loc['country_name'].encode('ascii', 'ignore') not in country:
        country.append(loc['country_name'].encode('ascii', 'ignore'))
    
print country
    