import sys
import dns.message
import dns.rdataclass
import dns.rdatatype
import dns.query
import dns.name
import dns.flags

domain="www.google.com"
ns="8.8.8.8"
rdclass=65535
domain=dns.name.from_text(domain)
if not domain.is_absolute():
	domain=domain.concatenate(dns.name.root)

request=dns.message.make_query(domain,dns.rdatatype.ANY)
request.flags |=dns.flags.AD
request.find_rrset(request.additional, dns.name.root, rdclass,
                   dns.rdatatype.OPT, create=True, force_unique=True)
response=dns.query.udp(request,ns)

print response.answer
print response.additional
print response.authority
