from distutils.filelist import findall
from email import header
import math
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt

url = 'https://www.infomoney.com.br/'

headers = { 
    'User-Agent'      : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
    'Accept'          : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
    'Accept-Language' : 'en-US,en;q=0.5',
    'DNT'             : '1', # Do Not Track Request Header 
    'Connection'      : 'close'
}

data = requests.get(url, headers=headers).text
soup = BeautifulSoup(data, "html.parse")


table = soup.find('table')
read = pd.read_html(match='maiores altas')

df = pd.DataFrame(columns=['Ação', 'Alta', 'Preço por ação'])

for row in table.tbody.find_all('tr'): 
    columns = row.find_all('td')  
    if(columns != []):
        acao = columns[0].text.strip(' ')
        alta = columns[1].text.strip(' ')
        preco = columns[2].text.strip(' ')
        df = pd.concat([df, pd.DataFrame.from_records([{'Ação': acao,  'Alta': alta, 'Preço': preco }])], ignore_index=True)

