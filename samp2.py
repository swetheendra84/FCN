import sys
import dns.message
import dns.rdataclass
import dns.rdatatype
import dns.query
import dns.name
import dns.flags

def fun(domain,dtype,ns,rdclass):
	if(dtype==1 or dtype==2 or dtype==15):
		domain=dns.name.from_text(domain)
		if not domain.is_absolute():
			domain=domain.concatenate(dns.name.root)
		request=dns.message.make_query(domain,dtype)
		request.flags |=dns.flags.AD
		request.find_rrset(request.additional, dns.name.root, rdclass,
                   dns.rdatatype.OPT, create=True, force_unique=True)
		for ip in ns :
			print "before response"
			response=dns.query.udp(request,ip)
			print "after response"
			if response is not None:
				return response
	else :
		print "Application supports only A MX NS"
		exit(-1);
if(len(sys.argv)<3):
	print "invalid number of arguments"
	exit(-1)
domain=sys.argv[1]
dtype=sys.argv[2]
typ=int(dtype)
rdclass=65535
ns=['198.41.0.4','192.228.79.201','192.33.4.12','199.7.91.13','192.203.230.10','192.5.5.241','192.112.36.4','198.97.190.53','192.36.148.17','192.58.128.30','193.0.14.129','199.7.83.42','202.12.27.33']
#ns=["8.8.8.8","8.8.4.4"]
resp=fun(domain,typ,ns,rdclass)
print resp
