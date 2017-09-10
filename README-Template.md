# sock0

Scraping the proxy table from socks-proxy.net, retrieves proxies from countries for various types of proxies (socks4, socks5). Returns IP address and Port

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need python3

You need to install bs4, so from pip3 do an install of bs4

```
sudo pip3 install bs4
```
## Examples

All proxies for the United States:
```
Mafdet:sock0 sgoyette$ python3 sock0.py
Enter the name of a country to get a list of proxies: United States
Enter the type of proxy (all, socks5, socks4): all
Socks5  24.165.56.120   54513
Socks5  24.115.150.190  31457
Socks5  97.81.230.65    29500
Socks5  73.119.56.91    34048
Socks5  99.130.95.17    51176
Socks5  64.53.148.34    10200
Socks5  75.143.111.221  53374
Socks5  68.190.240.211  16449
Socks5  65.104.194.251  30655
Socks5  23.28.248.249   17113
Socks4  198.186.15.135  10200
Socks5  173.22.1.185    22659
Socks5  68.178.128.103  8080
Socks5  70.88.3.13      45433
Socks5  104.228.154.96  10200
Socks5  23.28.23.232    10200
Socks5  24.214.52.144   55402
Socks5  173.26.244.42   44316
Socks5  73.36.169.89    15201
Socks5  68.197.182.252  11557
```
Socks5 proxies for Brazil:
```
Mafdet:sock0 sgoyette$ python3 sock0.py
Enter the name of a country to get a list of proxies: brazil
Enter the type of proxy (all, socks5, socks4): socks5
Socks5  181.220.169.20  18086
Socks5  181.222.42.233  50521
Socks5  181.223.251.197 15236
Socks5  181.222.42.91   50667
Socks5  200.229.202.123 1080
```

Socks4 proxies for the Russian Federation:
```
Mafdet:sock0 sgoyette$ python3 sock0.py
Enter the name of a country to get a list of proxies: russian federation
Enter the type of proxy (all, socks5, socks4): socks4
Socks4  149.154.69.82   3128
Socks4  83.172.0.69     1080
```

## Versioning

1.0

## Authors

* **k3rber0s**
