#!/usr/bin/env python

print('Scraping the beautiful soup...')

from bitlorean import *
jigaWatts = bitLorean()

if jigaWatts > 1.21:
    canit = "YES"
    trips = "That is enough for Marty McFly to travel Back to the Future %d times." % int(jigaWatts / 1.21)
else:
    canit = "NO"
    trips = "That is not enough for Marty McFly to travel Back to the Future."

print('Generating index.html...')
f = open('index.html', 'w')

html = """
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Can Bitcoin Power the DeLorean?</title>
  <link rel="stylesheet" href="style.css">
</head>

<body>
  <h1>Can Bitcoin Power the DeLorean?</h1>
  <h1>%s</h1>
  <h3>Bitcoin consumes %.2f jigaWatts of power. %s</h3>
  <p>Formula: <b><i>Implied Watts per GH/s</i></b> &#183; <b><i>Total Network Hashrate in GH/s</i></b></p>
  <p>Source: <a href=https://digiconomist.net/bitcoin-energy-consumption>https://digiconomist.net/bitcoin-energy-consumption</a></p>
</body>
</html>
""" % (canit, jigaWatts, trips)

f.write(html)
f.close()
print('Done!')
