import os, requests
from bs4 import BeautifulSoup
from collections import namedtuple

from flask import Flask, render_template

bitlorean = Flask(__name__)

BEC = 'https://digiconomist.net/bitcoin-energy-consumption'

def trips(jigawatts):
    can = ""

    if jigawatts > 1.21:
        can = "YES"
    else:
        can = "NO"

    return can

def marty(jigawatts):
    mcfly = ""

    if jigawatts > 1.21:
        mcfly =  "That is enough for Marty McFly to travel Back to the Future %d times." % int(jigawatts / 1.21)
    else:
        mcfly = "That is not enough for Marty McFly to travel Back to the Future."

    return mcfly

def bitLorean():
    source = requests.get(BEC)
    soup = BeautifulSoup(source.text, 'html.parser')

    def scrapeSoup(soup):
        jigaTuple = namedtuple('jigaTuple', 'Watts hashrate')

        impliedWatts = soup.find('tr', {'id': 'table_3_row_7'})
        impliedWatts = impliedWatts.find_all('td')[1].get_text()
        Watts = float(impliedWatts)  # Watts is never watts

        totalHashrate = soup.find('tr', {'id': 'table_3_row_8'})
        totalHashrate = totalHashrate.find_all('td')[1].get_text().replace(',', '')
        hashrate = float(totalHashrate) * (10 ** 6)  # convert PH/s to GH/s

        return jigaTuple(Watts=Watts, hashrate=hashrate)

    jigaWatts = scrapeSoup(soup)

    Watts = jigaWatts.Watts
    hashrate = jigaWatts.hashrate

    jigaBitcoins = ( Watts * hashrate ) / (10 ** 9)  # needs to be in jigaWatts

    return jigaBitcoins

#print('Bitcoin consumes %s jigaWatts of power...' % bitLorean())

@bitlorean.route('/')
def canbitcoinpowerthedelorean():
    jigawatts = bitLorean()

    return render_template("index.html", jigawatts=jigawatts, can=trips(jigawatts), mcfly=marty(jigawatts))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    bitlorean.run(host="0.0.0.0", port=port)
