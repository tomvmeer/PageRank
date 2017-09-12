import multiprocessing

def worker(d, key):
    d.append(key)

if __name__ == '__main__':
    urls = [10,20,30,40,50,60]
    mgr = multiprocessing.Manager()
    d = mgr.list()
    jobs = []
    for url in urls:
        jobs.append(multiprocessing.Process(target=worker, args=(d, url)))
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    for item in d:
        print(item)
