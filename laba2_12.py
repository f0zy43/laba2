import urllib.request
import time
import threading

urls = [
    'https://www.yandex.ru', 'https://www.google.com',
    'https://habrahabr.ru', 'https://www.python.org',
    'https://isocpp.org',
]

def read_url(url):
    with urllib.request.urlopen(url) as u:
        return u.read()

def fetch_urls(urls):
    results = []
    for url in urls:
        result = read_url(url)
        results.append(result)
    return results

# создаем и запускаем потоки
threads = []
num_threads = 4  # кол-во потоков
url_chunks = [urls[i:i + num_threads] for i in range(0, len(urls), num_threads)]
for chunk in url_chunks:
    thread = threading.Thread(target=fetch_urls, args=(chunk,))
    thread.start()
    threads.append(thread)

start = time.time()
for thread in threads:
    thread.join()

print(time.time() - start)