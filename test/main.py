# -*- coding: utf-8 -*-
"""
MAIN
"""
import json
import requests
from colorama import Back, init
init()

def run():
    r = requests.get('https://api.chucknorris.io/jokes/random')
    with open('json-joker.json', 'w') as dataFile:
        json.dump(r.json(), dataFile, indent=4)
    

    f = open('json-joker.json')

    c = json.loads(r.text)
    c = json.dumps(c)

    data = json.load(f)

    with open('joker.txt', 'w') as L:
        L.write(data['value'])
    
    print (Back.BLUE + c)
  
    f.close()

    

    return 0