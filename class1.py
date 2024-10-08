import http.client
from urllib.parse import urlsplit
import re

class Website:
    def __init__(self, url):
        self.url = url
        self.html = ""
        self.title = "[TITLE NOT FOUND]"

        try:
            conn = http.client.HTTPSConnection(urlsplit(self.url).netloc)
            conn.request("GET", urlsplit(self.url).path or "/")
            response = conn.getresponse()
            
            if response.status == 200:
                self.html = response.read().decode()
                
                match = re.search(r'<title>(.*?)</title>', self.html, re.IGNORECASE)
                self.title = match.group(1) if match else "[TITLE NOT FOUND]"
            else:
                self.title = f"{response.status} {response.reason}"

        except Exception as e:
            self.title = f"{str(e)}"

