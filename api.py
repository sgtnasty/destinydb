#!/usr/bin/env python3


import requests
import sys
import json

def main(apikey):
    #dictionary to hold extra headers
    HEADERS = {"X-API-Key": apikey}

    #make request for Gjallarhorn
    r = requests.get("https://www.bungie.net/platform/Destiny/Manifest/InventoryItem/1274330687/", 
        headers=HEADERS);

    #convert the json object we received into a Python dictionary object
    #and print the name of the item
    inventoryItem = r.json()
    print(inventoryItem['Response']['data']['inventoryItem']['itemName'])
    #print(repr(inventoryItem))
    #i = json.loads(inventoryItem)
    print(json.dumps(inventoryItem, indent = 4))
    #print(repr(inventoryItem))
    #Gjallarhorn


if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print('ERROR: need to provide Bungie API key as first argument')
        sys.exit(1)
    main(sys.argv[1])