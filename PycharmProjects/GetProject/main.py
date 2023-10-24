#subdomainlerin varlığını kontrol eden bir program. GOOGLE ÖRNEĞİ


import requests

def responseReguest(url):
    try:
        return requests.get(url)
    except:
        pass

googleurL = "google.com"

with open("word.txt" , "r") as reading:
    for word in reading:
        word = word.strip()
        url = "https://" + word + "." + googleurL
        response =  responseReguest(url)
        if response: #eğer response sonucu true ise yani [200] ise url'yi yazdıracak.
            print(url)
        else:
            pass





