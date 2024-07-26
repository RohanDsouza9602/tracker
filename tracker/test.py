import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
from common.utils import Utils
from common.constants import PRICE_SELECTOR_MAP
class SamplePriceExtractor():

    def __init__(self, website, product_url):
        self.website = website
        self.product_url = product_url
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            "Accept-Language": "em-GB,en-US;q=0.9,en;q=0.8"
        }

    def run(self):
        response = requests.get(self.product_url, self.header)
        if response.status_code!=404:
            filename = f"dumps/{Utils.md5_hash(self.product_url)}"
            with open(filename, "w") as file:
                file.write(str(response.content))

            soup = BeautifulSoup(response.content, "lxml")
            price = soup.find(class_=PRICE_SELECTOR_MAP.get(self.website)).get_text()
            print(f"DEBUG:::::PRICE:::::{price}")

if __name__ == '__main__':
    seiko_watch = SamplePriceExtractor("Flipkart", "https://www.flipkart.com/seiko-ssk003k1-5-sports-gmt-automatic-analog-watch-men/p/itma9133e1e5fd97?pid=WATGMHGZ26AUZPSJ&lid=LSTWATGMHGZ26AUZPSJGIFSMT&marketplace=FLIPKART&q=seiko+&store=search.flipkart.com&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=ba9caaa3-2e21-40c8-be92-8ab3a05ea8d9.WATGMHGZ26AUZPSJ.SEARCH&ppt=sp&ppn=sp&ssid=ehnscqc0a80000001722028192985&qH=700f447d143dbec5")
    seiko_watch.run()