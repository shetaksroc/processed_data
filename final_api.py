import csv
import datetime

import sys, json
try:
    data = json.loads(sys.argv[1])
except:
    print "ERROR"
    sys.exit(1)
l=[]
for i in data:
	l.append(i)


with open('d1_1.csv','r') as csv1:
	
	
	
	
		spamreader = csv.reader(csv1, delimiter=';', quotechar='|')
		spamwriter = csv.writer(csv1, delimiter=';', quotechar='|')
		a=[]
		for row in spamreader:
			l=row[0].strip("''").split(',')
			a.append(l)
		#print(a)	
			#print(l)
			#dt=row[9].strip('""')
			
with open('d1_1.csv','w') as csv2:
			spamwriter = csv.writer(csv2, delimiter=';', quotechar='|')
			for i in a:
				
			#print(l[5],l[6],l[7],wk,week_number)
				spamwriter.writerow([l[0],l[1],l[2],l[3],1,2])	


# Load the data that PHP sent us
# Generate some data to send to PHP
# Send it to stdout (to PHP)
print json.dumps(l)
