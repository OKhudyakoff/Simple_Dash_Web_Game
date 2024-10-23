def check_city(lastCity, newCity):
    if(lastCity == ''):
        return True
    if(newCity[0] == lastCity[-1]):
        return True
    return False