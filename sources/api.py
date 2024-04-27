import requests

COUNTRY_ENDPOINT= api_url = "https://restcountries.com/v3.1/name/{country_name}"

def get_country_info(country_name):
    
    response = requests.get(COUNTRY_ENDPOINT)
    if response.status_code == 200:
        country = response.json()[0]
        return country
    else:
        print(f"Couldn't find. {response.status_code}")
        return None
