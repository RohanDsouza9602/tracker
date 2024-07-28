import io
import requests
import lxml
from bs4 import BeautifulSoup
import smtplib
from common.utils import Utils
from common.constants import PRICE_SELECTOR_MAP
from price_parser import Price
import redis

class SamplePriceExtractor():

    def __init__(self, product_name, website, product_url):
        self.product_name = product_name
        self.website = website
        self.product_url = product_url
        self.header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            "Accept-Language": "em-GB,en-US;q=0.9,en;q=0.8"
        }
        self.redis_client = redis.Redis(password="admin")
        self.timeseries = self.redis_client.ts()

    def fetch_price_from_dump(self, filepath):
        with open(filepath, "r") as fp: 
            dump = fp.read()
        soup = BeautifulSoup(dump, "lxml")
        price = soup.find(class_=PRICE_SELECTOR_MAP.get(self.website)).get_text()
        print(f"DEBUG:::::PRICE-STRING:::::{price}")
        final_price = Price.fromstring(price)
        print(f"DEBUG:::::PRICE:::::{final_price}")
        return final_price.amount_float
        
    def add_tracker_to_redis(self, price: float):
        try:
            heartbeat = self.redis_client.ping()
            if heartbeat:
                self.timeseries.create("")
            else:
                print("Redis is not reachable")
        except Exception as e:
            print(f"Error {e}")

    def fetch_price_and_start_tracking(self):
        filepath = Utils.fetch_dump_from_url(self.product_url, self.header)
        price = self.fetch_price_from_dump(filepath)
        print(f"Price of the item is {price}.")
        
if __name__ == '__main__':  
    seiko_SSK003K1 = SamplePriceExtractor("Seiko SSK003K1", "Flipkart", "https://www.flipkart.com/seiko-ssk003k1-5-sports-gmt-automatic-analog-watch-men/p/itma9133e1e5fd97?pid=WATGMHGZ26AUZPSJ&lid=LSTWATGMHGZ26AUZPSJGIFSMT&marketplace=FLIPKART&q=seiko+&store=search.flipkart.com&srno=s_1_1&otracker=search&otracker1=search&fm=Search&iid=ba9caaa3-2e21-40c8-be92-8ab3a05ea8d9.WATGMHGZ26AUZPSJ.SEARCH&ppt=sp&ppn=sp&ssid=ehnscqc0a80000001722028192985&qH=700f447d143dbec5")
    seiko_SSK003K1.fetch_price_and_start_tracking()
    