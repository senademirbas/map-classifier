import random

def getCapital(country):
    print("Capital: ", country.get('capital'))

def getRegion(country):
    print("Region: ", country.get('region'))

def getCurrency(country):
    print("Currency: ", country.get('currency'))
    
def getPopulation(country):
    print("Population: ", country.get('population'))
    
def options(option, country):
    if option == '1':
        getCapital(country)
    elif option == '2':
        getCurrency(country)
    elif option == '3':
        getPopulation(country)
    elif option == '4':
        getRegion(country)
    else:
        print("Invalid content. Try again.")