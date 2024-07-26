import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

price_url = "https://www.flipkart.com/seiko-ssk003k1-5-sports-gmt-automatic-analog-watch-men/p/itma9133e1e5fd97?pid=WATGMHGZ26AUZPSJ&lid=LSTWATGMHGZ26AUZPSJGIFSMT&marketplace=FLIPKART&q=seiko+&store=search.flipkart.com&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=ba9caaa3-2e21-40c8-be92-8ab3a05ea8d9.WATGMHGZ26AUZPSJ.SEARCH&ppt=sp&ppn=sp&ssid=ehnscqc0a80000001722028192985&qH=700f447d143dbec5"
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Accept-Language": "em-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(price_url, headers=header)
print(response.content)

with open("file.txt", "w") as file:
    file.write(str(response.content))

soup = BeautifulSoup(response.content, "lxml")
price = soup.find(class_="Nx9bqj CxhGGd").get_text()
print(price)