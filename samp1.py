import sys
import dns.message
import dns.rdataclass
import dns.rdatatype
import dns.query
import dns.name
import dns.flags

def fun(domain,dtype,ns,rdclass):
	domain=dns.name.from_text(domain)
	if not domain.is_absolute():
		domain=domain.concatenate(dns.name.root)

	request=dns.message.make_query(domain,dtype)
	request.flags |=dns.flags.AD
	request.find_rrset(request.additional, dns.name.root, rdclass,
                   dns.rdatatype.OPT, create=True, force_unique=True)
	response=dns.query.udp(request,ns)
	return response

domain=sys.argv[1]
dtype=sys.argv[2]
typ=int(dtype)
ns=["198.41.0.4","199.9.14.201","192.33.4.12","199.7.91.13","192.203.230.10","192.5.5.241","192.112.36.4","198.97.190.53","192.36.148.17","192.58.128.30","193.0.14.129","199.7.83.42","202.12.27.33"]
rdclass=65535
ip="8.8.8.8"
resp=fun(domain,typ,ip,rdclass)
print resp
