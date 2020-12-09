#druga wersja programu z zagadnienia web scrapingu wykorzystująca dane ze strony HTML
import requests
from bs4 import BeautifulSoup

data = requests.get('https://pogoda.interia.pl/prognoza-szczegolowa-krakow,cId,4970')
if data.status_code == 200:
    soup = BeautifulSoup(data.content, 'html.parser')
    #print(soup.prettify())
    temp = soup.find('div', class_='weather-currently-temp-strict').text
    if int(temp[0]) and int(temp[1]):
        output = temp[0] + temp[1]
        if int(output)>= -30 and int(output)<40:
            print("Temperature in Cracow: ", output, "C")
        else:
            print("Wrong temperature")
    else:
        print("Recived data is not a value")
else:
    print("downloading HTML page error")


