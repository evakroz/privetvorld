from random import *

evas_tickers= []

for var in range(5):
    n = round(uniform(1500,3000), 2)
    evas_tickers.append(n)

print(evas_tickers)

# smallest = min(evas_tickers)
#
# print({smallest})
#
# largest = max(evas_tickers)
#
# print({largest})

# evas_tickers.sort(reverse=False)
# print(evas_tickers)
# print(evas_tickers[0])
# print(evas_tickers[9])