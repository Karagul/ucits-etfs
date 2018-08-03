import pandas as pd
import json
#pd.read_json("lse_text.json")
FILE = "file://localhost/home/ubuntu/km3/py/ucits-etfs/lse.json"
#with open("lse_text.json") as datafile:
#        data = json.load(datafile)
#        dataframe = pd.DataFrame(data)
df = pd.read_json(FILE, orient='columns')
vendors = df['issuer_name'].unique()
print(vendors)
