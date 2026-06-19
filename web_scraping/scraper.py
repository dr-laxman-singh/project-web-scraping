import sys
sys.stdout.reconfigure(encoding='utf-8')
import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://www.iplt20.com/auction/2022"
headers={
    "User-Agents":"Mozilla/5.0"
}
r=requests.get(url,headers= headers)
soup=BeautifulSoup(r.text,"lxml")
table=soup.find("table", class_="ih-td-tab w-100 auction-tbl")
title=table.find_all("th")
header=[i.text.strip() for i in title]
df=pd.DataFrame(columns=header)
rows=table.find_all("tr")
for i in rows[1:]:
    data=i.find_all("td")
    row=[tr.text.strip() for tr in data]
    l=len(df)
    df.loc[l]=row
print(df)
df.to_csv("IPL Auction Status 2022.csv",index=False,encoding="utf-8")


