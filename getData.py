import requests
import json

def cs20():
    getCs20Req = requests.get('https://steamcommunity.com/market/priceoverview/?appid=730&currency=2&market_hash_name=CS20%20Case').json()
    if getCs20Req["success"] == True:
        return getCs20Req["lowest_price"].replace("£", "")
    else:
        raise Exception("Could not access market price for cs20 case")

def clutch():
    getClutchReq = requests.get('https://steamcommunity.com/market/priceoverview/?appid=730&currency=2&market_hash_name=Clutch%20Case').json()
    if getClutchReq["success"] == True:
        return getClutchReq["lowest_price"].replace("£", "")
    else:
        raise Exception("Could not access market price for clutch case")

def dangerZone():
    getDangerZoneReq = requests.get('https://steamcommunity.com/market/priceoverview/?appid=730&currency=2&market_hash_name=Danger%20Zone%20Case').json()
    if getDangerZoneReq["success"] == True:
        return getDangerZoneReq["lowest_price"].replace("£", "")
    else:
        raise Exception("Could not access market price for danger zone case")

def fracture():
    getFractureReq = requests.get('https://steamcommunity.com/market/priceoverview/?appid=730&currency=2&market_hash_name=Fracture%20Case').json()
    if getFractureReq["success"] == True:
        return getFractureReq["lowest_price"].replace("£", "")
    else:
        raise Exception("Could not access market price for fracture case") 

def gamma2():
    getGamma2Req = requests.get('https://steamcommunity.com/market/priceoverview/?appid=730&currency=2&market_hash_name=Gamma%202%20Case').json()
    if getGamma2Req["success"] == True:
        return getGamma2Req["lowest_price"].replace("£", "")
    else:
        raise Exception("Could not access market price for fracture case") 

def horizon():
    getHorizonReq = requests.get('https://steamcommunity.com/market/priceoverview/?appid=730&currency=2&market_hash_name=Horizon%20Case').json()
    if getHorizonReq["success"] == True:
        return getHorizonReq["lowest_price"].replace("£", "")
    else:
        raise Exception("Could not access market price for fracture case") 

def snakebite():
    getSnakebiteReq = requests.get('https://steamcommunity.com/market/priceoverview/?appid=730&currency=2&market_hash_name=Snakebite%20Case').json()
    if getSnakebiteReq["success"] == True:
        return getSnakebiteReq["lowest_price"].replace("£", "")
    else:
        raise Exception("Could not access market price for fracture case") 

def vanguard():
    getVanguardReq = requests.get('https://steamcommunity.com/market/priceoverview/?appid=730&currency=2&market_hash_name=Operation%20Vanguard%20Weapon%20Case').json()
    if getVanguardReq["success"] == True:
        return getVanguardReq["lowest_price"].replace("£", "")
    else:
        raise Exception("Could not access market price for fracture case") 
 
def brokenFang():
    getBrokenFangReq = requests.get('https://steamcommunity.com/market/priceoverview/?appid=730&currency=2&market_hash_name=Operation%20Broken%20Fang%20Case').json()
    if getBrokenFangReq["success"] == True:
        return getBrokenFangReq["lowest_price"].replace("£", "")
    else:
        raise Exception("Could not access market price for fracture case")  

def prisma():
    getPrismaReq = requests.get('https://steamcommunity.com/market/priceoverview/?appid=730&currency=2&market_hash_name=Prisma%20Case').json()
    if getPrismaReq["success"] == True:
        return getPrismaReq["lowest_price"].replace("£", "")
    else:
        raise Exception("Could not access market price for fracture case") 

def prisma2():
    getPrisma2Req = requests.get('https://steamcommunity.com/market/priceoverview/?appid=730&currency=2&market_hash_name=Prisma%202%20Case').json()
    if getPrisma2Req["success"] == True:
        return getPrisma2Req["lowest_price"].replace("£", "")
    else:
        raise Exception("Could not access market price for fracture case")  

def stockholmChampAutograph():
    getStockholdChampAutographReq = requests.get('https://steamcommunity.com/market/priceoverview/?appid=730&currency=2&market_hash_name=Stockholm%202021%20Champions%20Autograph%20Capsule').json()
    if getStockholdChampAutographReq["success"] == True:
        return getStockholdChampAutographReq["lowest_price"].replace("£", "")
    else:
        raise Exception("Could not access market price for fracture case")