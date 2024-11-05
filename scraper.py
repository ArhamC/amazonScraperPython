import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Bose-QuietComfort-45-Bluetooth-Canceling-Headphones/dp/B098FKXT8L?th=1"
custom_headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0'
    ,'accept-language' : 'en-US,en;q=0.9'
}

response = requests.get(URL, headers=custom_headers)

soup = BeautifulSoup(response.text, 'html.parser')

title_element = soup.select_one('#productTitle')

title = title_element.text.strip()

price_element = soup.select_one('span.a-offscreen')

print(title)
print(price_element.text)
