import math 
 
def rinkislaukums (rad):
    laukrink = math.pi*rad*rad 
    return laukrink

def rinkislinijagarums (rad):
    rinklin = (math.pi*2*rad)
    return rinklin

def radiussnolinijas (radlin):
    radgar = (radlin//(2*math.pi))
    return radgar

def radiussnolaukumaa (radlauk):
    radgarr = (math.sqrt(radlauk/math.pi))
    return radgarr