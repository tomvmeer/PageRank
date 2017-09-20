import urllib.request
import multiprocessing
import Matrix


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
    if urls == []:
        return False
    if urls == None:
        return False
    isolated = []
    for url in urls:
        try:
            isolated.append(isolate(url))
        except IndexError:
            pass
    host_counter = {}
    for element in isolated:
        if element != None:
            try:
                host_counter[element] = int(host_counter[element]) + 1
            except:
                host_counter[element] = 1
    if host_counter == {}:
        return False
    elif host_counter == "":
        return False
    else:
        return host_counter


def go_to(link):
    urls = []
    try:
        data = str(urllib.request.urlopen(link).read())
    except:
        return False
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


def worker(d, url):
    counted = go_to("http://www."+str(url))
    if counted != None or counted != False:
        if counted:
            counted["from"] = url
            d.append(counted)


if __name__ == '__main__':
    # Starting point of crawler:
    website = "http://www.startpagina.nl"
    counted = go_to(str(website))
    if counted == False:
        print("No internet")
    to_do = counted
    # Pre loop variables:
    data = Matrix.NewMatrix(1, 1)
    froms = []
    unique_urls = []
    error = 0
    done_total = 0
    x = 0
    y = 0
    # Main loop:
    mgr = multiprocessing.Manager()
    d = mgr.list()
    jobs = []
    for url in to_do:
        jobs.append(multiprocessing.Process(target=worker, args=(d, url)))
    print(len(to_do))
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    # Done multi threading
    done = 0
    to_do = []
    for item in d:
        if item["from"] not in froms:
            if x == data.w:
                data.new_column()
            froms.append(item["from"])
            for url in item:
                if url not in unique_urls:
                    if url != "from" and url != None:
                        if y == data.h:
                            data.new_row()
                        unique_urls.append(url)
                        to_do.append(url)
                        data.set(item[url],x,y)
                        y += 1
                        done += 1
                elif url != None:
                    y1 = unique_urls.index(url)
                    x1 = froms.index(item["from"])
                    data.set(item[url] + data.matrix[y1][x1] , x1, y1)
        else:
            error += 1
        x += 1
    data.print_out()
    print(len(unique_urls),data.h)
    print(len(froms), data.w)

