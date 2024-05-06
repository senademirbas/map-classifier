import requests

api_url = "https://restcountries.com/v3.1/all"
response = requests.get(api_url)
countries = response.json()

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
        print("Invalid content. Try again. ")
    

def get_info():
    is_continue = True
    while is_continue:
        if response.status_code == 200:
            print("1- Capital")
            print("2- Currency")
            print("3- Population")
            print("4- Region")
            print("5- Exit")
            
            option = input("Choose one: 1-2-3-4-5 ")

            if option == '5':
                is_continue = False
                break

            options(option, countries[0])
        
        elif response.status_code == 404:
            print(f"{country} couldn't find. ")
            break

        else:
            print("Unexpected error. ")
            break

if __name__ == "__main__":
    get_info()
