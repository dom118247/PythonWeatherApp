import requests
from urllib.parse import quote_plus  


def get_weather(city, api_key):
    
    city_encoded = quote_plus(city)
    
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_encoded}&appid={api_key}&units=metric"
    
    
    print(f"URL: {url}")  
    
    
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        
        # Extract weather details
        city_name = data['name']
        country = data['sys']['country']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        
        # Display the weather information
        print(f"Weather in {city_name}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather_description}")
    else:
        # Print the detailed error message for debugging
        print(f"Error: {response.status_code}")
        print(f"Message: {response.json()['message']}")


def main():
    
    api_key = "a3d47c1650a61ed2e5439dbdda3c6bdd" 
    
    
    city = input("Enter the name of the city: ")
    
    
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
