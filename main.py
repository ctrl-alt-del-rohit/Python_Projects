import requests

url = "https://api.tomorrow.io/v4/weather/realtime?"
apikey =str(input("Enter your apikey: "))
location= str(input('Enter the location: '))
headers = {"accept": "application/json"}
params = {
    "apikey": apikey,
    "location": location
}

def get_response(url):
    response = requests.get(url, headers=headers,params=params)
    return response.json()

def Get_weather_data(data):
    for key, value in data.items():
        
        return(f"{key}: {value}")

details=get_response(url)
print("Location:",details["location"])
print("Weather info: ",Get_weather_data(details))