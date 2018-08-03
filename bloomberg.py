import json
import urllib.request

url="https://www.bloomberg.com/markets/api/comparison/data?securities=GTII5:GOV,GTII10:GOV,GTII20:GOV,GTII30:GOV&securityType=GOVERNMENT_BOND_US&locale=en"
url="https://www.bloomberg.com/markets/api/comparison/data?securities=GTII5:GOV,GTII10:GOV,GTII20:GOV,GTII30:GOV&securityType=GOVERNMENT_BOND_US&locale=en"

res = urllib.request.urlopen(url)
res_body = res.read()
print(res_body)

# https://docs.python.org/3/library/json.html
j = json.loads(res_body.decode("utf-8"))
print(j)
