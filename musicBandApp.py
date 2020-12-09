import requests
import json

#API_consmer_key="OwnwELsGQUVKUdNgZAhQ"
#API_consumer_secret="ydDlAFPBIdrzSMrtdZLjlFymcoxhQcEa"
#program wymaga wprowadzenia nazwy zespolu z duzej litery
def urlMaker(artist_name):
    basicURL="https://api.discogs.com/database/search?&key=OwnwELsGQUVKUdNgZAhQ&secret=ydDlAFPBIdrzSMrtdZLjlFymcoxhQcEa&q="
    URL=f"{basicURL}{artist_name}"
    return URL

def urlRequest(URL):
    req = requests.get(URL)
    if req.status_code == 200:
        return req
    else:
        print("Connection error")
        return -1

def getArtistURL(req,artist_name):
    result = json.loads(req.text)
    #print(json.dumps(result, indent=4, sort_keys=True))
    artist = dict()
    for item in result['results']:
        name = item['title']
        resourceURL=item['resource_url']
        if item['type']=="artist":
            artist[name]=resourceURL
    if artist_name in artist:
        print(artist[artist_name])
        return artist[artist_name]

    else:
        print("No such band")
        return

def getMembers(url):
    result = json.loads(url.text)
    artist = dict()
    for item in result['members']:
        name = item['name']
        resourceURL=item['resource_url']
        artist[name] = resourceURL
    print(artist)
    return artist

def bandsEachPlayed(artist):
    for item in artist:
       url = artist[item]
       code = urlRequest(url)
       if code == -1:
           print("An error occurred while retrieving data ")
           return -1
       else:
           result = json.loads(code.text)
           list = []
           for groups in result['groups']:
               list.append(groups['name'])
               artist[item]=list

def bandCheck(dictionary):
    band = dict()
    temp = []
    membersList = []
    for item in dictionary:
        temp = dictionary[item]
        s = set()
        for item2 in dictionary:
            if item != item2:
                for element in temp:
                    if element in dictionary[item2]:
                        membersList.append(element)
                if len(membersList)>0:
                    for i in membersList:

                        if i in band:
                            tmp = set()
                            tmp = band[i]
                            tmp.add(item)
                            tmp.add(item2)
                            band[i]=tmp

                        else:
                           band[i]=set()
                           band[i]={item,item2}

                membersList.clear()

    for bandname in band:
        print(" ")
        print(f"{'Zespół: '}{bandname}")
        print(" ")
        for members in band[bandname]:
            print(members)


def main():
    artist_name = str(input('Wprowadz zespol, dla ktorego chcesz sprawdzic przynaleznosc czlonkow do innych zespolow (z dużych liter): '))
    print("Dane kontrolne: ")
    URL = urlMaker(artist_name)
    data = urlRequest(URL)
    if data == -1:
        print("URL error")
        return
    bandURL = getArtistURL(data,artist_name)
    data = urlRequest(bandURL)

    artist = dict()
    artist = getMembers(data)
    k = bandsEachPlayed(artist)
    if k==-1:
        return
    print(artist)
    bandCheck(artist)



if __name__ == '__main__':
    main()


