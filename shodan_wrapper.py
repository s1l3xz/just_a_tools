import shodan
import dns.resolver



SHODAN_API_KEY = "your shodan API key"

api = shodan.Shodan(SHODAN_API_KEY)


domains = [
#add domain here:
#example:
#my_super_domain.com,
]




def domain_resolver(domain_list):
    resolved_ip = []
    broked_domain = []
    for i in domain_list:
        try:
            for rdata in dns.resolver.query(i) :
                resolved_ip.append(rdata)
        except:
            broked_domain.append(i)
            continue

    if broked_domain.__sizeof__() > 0:
        print "not resolved domain"
        for domain in broked_domain:
            print domain

    print "start shodan scan"
    for domain in resolved_ip:
        print "A"*100
        shodan_scan_full(domain)
        print "B" * 100

def shodan_scan_full(ip):
    print ip
    try:
        host = api.host(str(ip))
        for i in host:
            print """%s: %s""" %(i, host[i])

    except:
        print "Error: No information available for that IP."
if __name__ == "__main__":
    domain_resolver(domains)