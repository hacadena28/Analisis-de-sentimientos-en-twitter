import random



def randlatlat():
    return str(round(random.uniform( -90,  90), 7))
print(randlatlat())    
    
def randlatlon():
    return round(random.uniform(-180, 180), 5)
print(randlatlon())       

    



 