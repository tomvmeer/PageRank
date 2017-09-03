import urllib2
data = urllib2.urlopen("https://nl.wikipedia.org/wiki/Vissen_(dieren)").read()
urls = []
for i in range(1,len(data.split("href="))):
    if "http" in ((data.split("href="))[i]):
        try:
            urls.append("http://"+(((data.split("href="))[i]).split('"')[1]).split("//")[1])
        except:
            pass
f = open("urls.txt","w")
for i in urls:
    f.write(i+"\n")
f.close()