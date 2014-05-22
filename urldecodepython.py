import urllib
server = "http://10.9.102.108:8000/"
url_file=open("links2")
#urls_dec = []
#urls_code = []
for line in url_file:
    #if line.__len__() > 0:
    #    urls_dec.append(urllib.unquote(line.rstrip('\n')))
    #    urls_code.append(line.rstrip('\n'))
    urllib.urlretrieve(server+line.rstrip('\n'),urllib.unquote(line.rstrip('\n')))

#for download in urls_code:
#    urllib.urlretrieve(server+download,urllib.unquote(download))
