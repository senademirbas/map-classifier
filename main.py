
from sources.api import get_country_info
from sources.functions import options, getCapital, getCurrency, getPopulation, getRegion

def get_info():
    while True:
        country_name = input("Type the country you want information (press 5 to quit):  ")
        if country_name.lower() == '5':
            break
        
        country = get_country_info(country_name)
        if country_name.lower() != '5':
            print("1- Capital")
            print("2- Currency")
            print("3- Population")
            print("4- Region")
            option = input("Choose one: 1-2-3-4 ")

            options(option, country)

if __name__ == "__main__":
    get_info()
