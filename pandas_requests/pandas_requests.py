import requests as rq
import pandas as pd

url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=100&sortBy=market_cap&sortType=desc&convert=USD,BTC,ETH&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap"
response = rq.request("GET", url)
data = response.json()

res = [p for p in data["data"]["cryptoCurrencyList"]]

try:
    data_frame = pd.json_normalize(res) 
    data_frame.to_csv("result.csv")
    print("It is done!")
except Exception as e:
    print("Something is wrong. Try again.", e)