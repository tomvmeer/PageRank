import urllib.request
import multiprocessing
import time


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
            host_counter[element] = 1
    return host_counter


def go_to(link):
    urls = []
    try:
        data = str(urllib.request.urlopen(link).read())
    except:
        return ""
    else:
        for i in range(1, len(data.split("href="))):
            if "http" in ((data.split("href="))[i]):
                try:
                    url = ("http://"+(((data.split("href="))[i]).split('"')[1]).split("//")[1])
                    if url not in urls:
                        urls.append(url)
                except:
                    pass
        return count(urls)


website = "http://startpagina.nl"
counted = go_to(str(website))
data = []
start = time.time()
for url in counted:
    data.append(go_to("http://www." + str(url)))
print(data)
print("")
print(time.time() - start)


def worker(d, url):
    counted = go_to("http://www."+str(url))
    if counted:
        counted["from"] = url
        d.append(counted)


if __name__ != '__main__':
    start = time.time()
    mgr = multiprocessing.Manager()
    d = mgr.list()
    jobs = []
    for url in counted:
        jobs.append(multiprocessing.Process(target=worker, args=(d, url)))
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    for item in d:
        print(item)
    print("")
    print(time.time()-start)
