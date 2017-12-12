import requests
from bs4 import BeautifulSoup
from collections import namedtuple

BEC = 'https://digiconomist.net/bitcoin-energy-consumption'

def bitLorean():
    source = requests.get(BEC)
    soup = BeautifulSoup(source.text, 'html.parser')

    def scrapeSoup(soup):
        jigaTuple = namedtuple('jigaTuple', 'Watts hashrate')
        
        impliedWatts = soup.find('tr', {'id': 'table_3_row_5'})
        impliedWatts = impliedWatts.find_all('td')[1].get_text()
        Watts = float(impliedWatts)  # Watts is never watts

        totalHashrate = soup.find('tr', {'id': 'table_3_row_6'})
        totalHashrate = totalHashrate.find_all('td')[1].get_text().replace(',', '')
        hashrate = float(totalHashrate) * (10 ** 6)  # convert PH/s to GH/s

        return jigaTuple(Watts=Watts, hashrate=hashrate)
    
    jigaWatts = scrapeSoup(soup)

    Watts = jigaWatts.Watts
    hashrate = jigaWatts.hashrate

    jigaBitcoins = ( Watts * hashrate ) / (10 ** 9)  # needs to be in jigaWatts

    return jigaBitcoins

print('Bitcoin consumes %s jigaWatts of power...' % bitLorean())
