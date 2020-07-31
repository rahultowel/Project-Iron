import pandas as pd
from pytrends.request import TrendReq

pytrends=TrendReq(hl='en-US',tz=360)

kw_list=["Quantum Computing"]
pytrends.build_payload(kw_list=kw_list, timeframe='today 5-y')

related=pytrends.related_queries()
print(related[kw_list[0]]['rising'])
