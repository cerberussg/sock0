import requests
from bs4 import BeautifulSoup
'''
Name: sock0.py
Author: k3rber0s
Date: 09/07/2017
Email: k3rber0s.c3rber0s@gmail.com
'''
class ProxyList:
    def __init__(self):
        self.country = 'United States'
        self.proxyType = 'Socks5'
        self.socks5 = requests.get("https://www.socks-proxy.net/")
        self.html = self.socks5.content
        self.soup = BeautifulSoup(self.html, "html.parser")
        self.socksList = self.soup.find_all("td")
        self.listCount = len(self.socksList)

    # Pulls the correct proxy type for the country user has entered.
    def getProxy(self):
        yesProxy = 0
        while proxy.listCount != 0:
            if proxy.proxyType == 'ALL':
                if proxy.socksList[3].text.upper() == proxy.country:
                    yesProxy += 1
                    print(proxy.socksList[4].text + "\t" + proxy.socksList[0].text + "\t" + proxy.socksList[1].text)
            elif proxy.proxyType == 'SOCKS5':
                if proxy.socksList[3].text.upper() == proxy.country and proxy.socksList[4].text.upper() == proxy.proxyType:
                    yesProxy += 1
                    print(proxy.socksList[4].text + "\t" + proxy.socksList[0].text + "\t" + proxy.socksList[1].text)
            elif proxy.proxyType == 'SOCKS4':
                if proxy.socksList[3].text.upper() == proxy.country and proxy.socksList[4].text.upper() == proxy.proxyType:
                    yesProxy += 1
                    print(proxy.socksList[4].text + "\t" + proxy.socksList[0].text + "\t" + proxy.socksList[1].text)

            # Deletes the first 8 values from the soup
            del proxy.socksList[0:8]
            proxy.listCount = len(proxy.socksList)

        if yesProxy == 0:
            print("No proxies found, try again!")
    # Needs a copy to clipboard function, would be super sweet to have the output copied already

proxy = ProxyList()
proxy.country = input("Enter the name of a country to get a list of proxies: ").upper()
proxy.proxyType = input("Enter the type of proxy (all, socks5, socks4): ").upper()
proxy.getProxy()
