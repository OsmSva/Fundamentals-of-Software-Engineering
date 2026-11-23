import requests
import json
from pprint import pprint

resp = requests.get('https://catalog.onliner.by/sdapi/catalog.api/search/dram?group=0&group_limit=0&limit=30&dramkit%5B0%5D=ddr4dimm&dramkit%5B1%5D=ddr4sodimm&dramkit%5Boperation%5D=union')
data = resp.json()

for product in data["products"]:
    ID = product["id"]
    FULL_NAME = product["full_name"]
    if FULL_NAME.rfind("DDR") != -1:
        ddr_idx = FULL_NAME.rfind("GB")
        ddr_idx_x2 = FULL_NAME.efind("2x")
        #if ddr_idx_x2 != -1:
            
        pprint(f"{ID}: ")
        
