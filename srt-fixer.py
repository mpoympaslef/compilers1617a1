import sys
import re
import argparse

		
parser = argparse.ArgumentParser()
# add mandatory (positional) arguments
parser.add_argument("fname",help="input srt file name")
parser.add_argument("offset",type=float,help="subtitle offset in seconds to apply (can be fractional)")

# parse arguments
args = parser.parse_args()

secs = args.offset

with open(args.fname,newline='') as ifp:	
	for line in ifp:
		
		res = re.search('-->',line)
		
		if res == None:
			# -- αντικαταστήστε με τον δικό σας κώδικα (αρχή) --
			sys.stdout.write(line)
		else:
			# -- αντικαταστήστε με τον δικό σας κώδικα (τέλος) --
			
			times = re.split('-->',line)
			import datetime
			
			str_date1=times[0].strip()
			str_date2=times[1].strip()
			
			fmt='%H:%M:%S,%f'
			date1 = datetime.datetime.strptime(str_date1, fmt)
			date2 = datetime.datetime.strptime(str_date2, fmt)
			
			
			date1 = date1 + datetime.timedelta(0,secs)
			date2 = date2 + datetime.timedelta(0,secs)
			
			str_date1 = str(date1.time())
			str_date1 = str_date1.replace('.',',')
			str_date1 =str_date1[0:len(str_date1)-3]
			
			str_date2 = str(date2.time())
			str_date2 = str_date2.replace('.',',')
			str_date2 =str_date2[0:len(str_date2)-3]
			
			line = str_date1+' --> '+str_date2+'\n'
			sys.stdout.write(line)
