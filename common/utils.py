import hashlib
import io
import os
from bs4 import BeautifulSoup
import requests

class Utils():
    
    @staticmethod  
    def md5_hash(
        input_string: str
    ):
        md5_hash_object = hashlib.md5()
        md5_hash_object.update(input_string.encode("utf-8"))
        hash_result = md5_hash_object.hexdigest()
        return hash_result
    
    @staticmethod
    def fetch_dump_from_url(
        url: str, 
        headers: dict | None = None
    ):
        try:
            response = requests.get(url, headers, timeout=5)
            if response.status_code!=404:
                os.makedirs('dumps', exist_ok=True)
                filepath = f"dumps/{Utils.md5_hash(url)}"
                with open(filepath, "w", encoding='utf-8') as file:
                    file.write(response.text)
                return filepath 
            else:
                print(f"ERROR:::::STATUS CODE {response.status_code}")
        except Exception as e:
            print(f"DEBUG:::::ERROR:::::FAILED TO FETCH URL {url} - {e}")