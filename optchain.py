from http.client import responses

import requests
import pandas as pd
import time

NSE_HOME = 'https://www.nseindia.com'
NIFTY = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'accept-encoding' : 'gzip, deflate, br, zstd',
    'accept-language' : 'en-US,en;q=0.9,hi;q=0.8',
    'referer': NSE_HOME
}

session = requests.Session()
request = session.get(NSE_HOME, headers=headers)
time.sleep(18)

cookies = dict(request.cookies)
response = session.get(NIFTY, headers=headers, cookies=session.cookies)
#print(response)  # Print response to check content

print(response.status_code)
print(response.json())


