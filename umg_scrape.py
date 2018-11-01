'''

This short program utilizes the tools of requests, beautiful soup and pandas in order to web scrape information from the leaderboards
of UMG Gaming and packages it to be useful for analysis. 

'''

import requests
import bs4 as bs
import pandas as pd

# FIRST IMPLEMENTATION

url = "https://umggaming.com/leaderboards"
header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest"
         }

data = requests.get(url, headers = header)
dfs = pd.read_html(data.text)
for df in dfs:
    print(df)
        

# SECOND IMPLEMENTATION
url = "https://umggaming.com/leaderboards"
data = requests.get(url)

soup = bs.BeautifulSoup(data.text, "html.parser")

# site_text= soup.get_text()
# print(site_text)

leaderboard = soup.find("table", {"id": "leaderboard-table"})
tbody = leaderboard.find("tbody")

for tr in tbody.find_all("tr"):
    place = tr.find_all("td")[0].text.strip()
    username = tr.find_all("td")[1].find_all("a")[1].text.strip()
    xp = tr.find_all("td")[3].text.strip()

    print(place, username, xp)