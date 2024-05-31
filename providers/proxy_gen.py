import threading
import queue
import requests
from config import *
import os
import re
from bs4 import BeautifulSoup

class ProxyGenerator:
    def __init__(self) -> None:
        self._q = queue.Queue()
    
    def _scrape_proxies(self):
        source = str(requests.get(PROXIES_URL, headers=PROXY_HEADERS, timeout=10).text)
        soup = BeautifulSoup(source, 'html.parser')
        proxy_row_tags = soup.find_all('tr')[1:]
        ips = []
        ports = []
        print(len(proxy_row_tags))
        proxy_rows = []
        
        for row in proxy_row_tags:
            ip = row.find_all('td')
            if ip:
                ip = ip[0].text
                ips.append(ip)
                port = row.find_all('td')
                if port:
                    port = port[1].text
                    ports.append(port)
                    proxy_rows.append(f"{ip}:{port}")

        print(f"scraped {len(proxy_rows)} proxies")
        with open(PROXIES, 'w') as f:
            for proxy in proxy_rows:
                f.write(proxy + '\n')
    
    def _load_proxies(self):
        with open(PROXIES, 'r') as f:
            self._proxies = f.read().split('\n')
            for p in self._proxies:
                self._q.put(p)
    
    def _check_proxies(self):
        while not self._q.empty():
            proxy = self._q.get()
            try:
                response = requests.get(
                    PROXY_TEST_URL,
                    proxies = {"http": proxy,
                            "https": proxy},
                    timeout=5 # set a timeout for the request
                )
            except:
                continue
            if response.ok:
                print(proxy)
                with open(VALID_PROXIES, 'a') as f: # append the proxy to file
                    f.write(proxy + '\n')

    def _generate_valid_proxies(self):
        self._load_proxies()
        # Delete old file if it exists
        if os.path.exists(VALID_PROXIES):
            os.remove(VALID_PROXIES)

        threads = []
        for _ in range(N_OF_THREADS):
            t = threading.Thread(target=self._check_proxies)
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

    def get_valid_proxies(self, scrape=False):
        if scrape:
            self._scrape_proxies()
            self._generate_valid_proxies()
        validProxies = []
        with open(VALID_PROXIES, 'r') as f:
            proxies = f.read().split('\n')
            for proxy in proxies:
                if len(proxy) > 0:
                    validProxies.append(proxy)
        return validProxies