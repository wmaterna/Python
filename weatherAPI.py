#do pobierania danych używam api https://openweathermap.org/api z wygenerowanym swoim id wklejonym w poniższy url, dostaje w ten sposob JSONowe dane pogodowe dla konkretnego miasta

import requests
import json

def urlRequest(cityName):
    basicURL = "https://api.openweathermap.org/data/2.5/weather?&appid=e54be9c68963caa3cb8cd4f9210a4e5d&units=metric&q="
    URL = f"{basicURL}{cityName}"
    req = requests.get(URL)
    if req.status_code==200:
        return req
    else:
        return -1

def parsingJson(req):
    result = json.loads(req.text)
    # print(json.dumps(result, indent=4, sort_keys=True))
    tempValue = result['main']['temp']
    if tempValue < 50 or tempValue > -50:
        print(tempValue)

def main():
    cityInput = str(input('Wprowadz miasto, dla ktorego chcesz sprawdzic pogode: '))
    data = urlRequest(cityInput)
    if data == -1:
        print('URL connection error')
    parsingJson(data)

if __name__ == '__main__':
    main()
