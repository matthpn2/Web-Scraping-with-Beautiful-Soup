'''

This short program utilizes the tools of requests and beautiful soup in order to web scrape information from the products page of Newgg
and parses it into a useful csv data file for analysis.

'''

import requests
import bs4 as bs

headers = "brand, product_name, shipping\n"

filename = "products.csv"
f = open(filename, "w")
f.write(headers)

url = "https://www.newegg.com/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphics+cards&N=-1&isNodeId=1"
data = requests.get(url)

soup = bs.BeautifulSoup(data.text, "html.parser")

products = soup.find_all("div", {"class": "item-container"})
for product in products:
    brand = product.div.div.a.img["title"]
    product_name = product.find("a", {"class": "item-title"}).text.strip()
    shipping = product.find("li", {"class": "price-ship"}).text.strip()

    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)

    f.write(brand.replace(",", " ") + "," + product_name.replace(",", "|") + "," + shipping + "\n")

f.close()