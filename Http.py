import urllib2

def goto(link,urls):
    data = urllib2.urlopen(link).read()
    urls.append("outgoing from:"+str(link))
    for i in range(1,len(data.split("href="))):
        if "http" in ((data.split("href="))[i]):
            try:
                url = ("http://"+(((data.split("href="))[i]).split('"')[1]).split("//")[1])
                if url not in urls:
                    urls.append(url)
            except:
                pass
    return urls

urls = goto("http://nl.wikipedia.org/w/index.php?title=Vissen_(dieren)&amp;oldid=49574769",[])
for i in urls:
    try:
        goto(i,urls)
        f = open("urls.txt","w")
        for url in urls:
            f.write(str(url)+"\n")
        f.close()
        print(len(urls))
    except:
        pass

