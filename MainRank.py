import urllib.request

def isolate(url):
    isolated = None
    raw = url.split("www.")[1]
    webpage = raw.split(".")[0]
    domain = raw.split(".")[1].split("/")[0]
    f = open("domains.txt")
    for line in f.read().split("\n"):
        if domain == line:
            isolated = (webpage + "." + domain)
    f.close()
    return isolated

def count(urls):
    isolated = []
    for url in urls:
        try:
            isolated.append(isolate(url))
        except IndexError:
            pass

    host_counter = {}
    for element in isolated:
        try:
            host_counter[element] = int(host_counter[element]) + 1
        except:
            host_counter[element] = 0
    return host_counter


def go_to(link, urls):
    data = str(urllib.request.urlopen(link).read())
    for i in range(1,len(data.split("href="))):
        if "http" in ((data.split("href="))[i]):
            try:
                url = ("http://"+(((data.split("href="))[i]).split('"')[1]).split("//")[1])
                if url not in urls:
                    urls.append(url)
            except:
                pass
    return count(urls)

print(go_to("http://www.startpagina.nl/",[]))
