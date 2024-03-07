import requests
from lxml import html
import pandas as pd

YEAR = 2024
URL = f'https://www.ft.com/ft1000-{YEAR}'
OUTPUT = "data/ft1000-2024_requests.csv"
headers = {
    'authority': 'www.ft.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'en-US,en;q=0.9',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Brave";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
}

response = requests.get(URL, headers=headers)
page = html.fromstring(response.text)
table_rows = page.xpath("//tbody/tr")
columns = page.xpath("//thead/tr//text()")
table_data = []
for table_row in table_rows:
  table_data_row = table_row.xpath(".//td//text()")
  table_data.append(table_data_row)
df = pd.DataFrame(table_data, columns=columns)
df.to_csv(OUTPUT, index=False)
