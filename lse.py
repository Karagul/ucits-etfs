# LSE Download spreadsheet of all isntruments
# save them in json format

import urllib.request
import xlrd
import json
from collections import OrderedDict
FILE = "lse.xlsx"
FILE_JSON = "lse.json"

def download_instruments():
    url = "https://www.londonstockexchange.com/statistics/companies-and-issuers/instruments-defined-by-mifir-identifiers-list-on-lse.xlsx"
    urllib.request.urlretrieve(url, FILE)

book = xlrd.open_workbook( FILE )
###############
# process etfs
sh = book.sheet_by_name("1.3 ETFs")
#print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
#print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))
tickers_etfs = []
store_flag = 0
for rx in range(sh.nrows):
    if store_flag == 1:
        ticker = OrderedDict()
        ticker['ticker'] = sh.row(rx)[0].value
        ticker['issuer_name'] = sh.row(rx)[1].value
        ticker['instrument_name'] = sh.row(rx)[2].value
        ticker['isin'] = sh.row(rx)[3].value
        ticker['mifir_identified_code'] = sh.row(rx)[4].value
        ticker['start_date'] = sh.row(rx)[5].value
        ticker['country_of_incorporation'] = sh.row(rx)[6].value
        ticker['ccy'] = sh.row(rx)[7].value
        if ticker['ccy']:
            tickers_etfs.append(ticker)
    if sh.row(rx)[0].value == "TIDM":
        store_flag = 1
###############
# process etfs
sh = book.sheet_by_name("2.2 ETCs")
tickers_etcs = []
store_flag = 0
for rx in range(sh.nrows):
    if store_flag == 1:
        ticker = OrderedDict()
        ticker['ticker'] = sh.row(rx)[0].value
        ticker['issuer_name'] = sh.row(rx)[1].value
        ticker['instrument_name'] = sh.row(rx)[2].value
        ticker['isin'] = sh.row(rx)[3].value
        ticker['mifir_identified_code'] = sh.row(rx)[4].value
        ticker['start_date'] = sh.row(rx)[7].value
        ticker['country_of_incorporation'] = sh.row(rx)[9].value
        ticker['ccy'] = sh.row(rx)[10].value
        if ticker['ccy']:
            tickers_etfs.append(ticker)
    if sh.row(rx)[0].value == "TIDM":
        store_flag = 1

# write them to file
j_etfs = json.dumps(tickers_etfs, sort_keys=True, indent=4)
j_etcs = json.dumps(tickers_etcs, sort_keys=True, indent=4)
with open(FILE_JSON, 'w') as f:
        f.write(j_etfs)
        f.write(j_etcs)
