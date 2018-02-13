import requests


ip_address_list = [
#add domain here:
#example:
#my_super_domain.com,
]


bad_address = []
timeout = 2
contentSize = 300
for i in ip_address_list:
    try:
        repHttp = requests.get('http://' + i, timeout = timeout )
        if (len(repHttp.content) > contentSize):
            print "web http " + i

        repHttps = requests.get('https://' + i, timeout = timeout)
        if (len(repHttps.content) > contentSize):
            print "web https " + i
    except:
        bad_address.append(i)
        continue


if len(bad_address) > 0:
    print "not a web"
    for i in bad_address:
        print i