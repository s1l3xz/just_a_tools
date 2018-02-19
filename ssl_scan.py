import ssl
import OpenSSL


cert = ssl.get_server_certificate(('www.google.com', 443))
x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
print x509.has_expired()
print "suport encryption support : " + x509.get_signature_algorithm()
print "version : " + str(x509.get_version()) + "\n"

for i in range(x509.get_extension_count()):
    print str(x509.get_extension(i)).replace(',', '\n')

