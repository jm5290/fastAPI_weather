from fastapi import FastAPI

app  = FastAPI() ; 

@app.get('/get-weather/{cityn}/{scale}')
async def get_weather(cityn: str, scale: str):

    import requests

    # Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
    API_KEY = '6c56d510f76d209a14f2d6082683e152'

    # Define the base URL for the OpenWeatherMap API
    BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

    # Specify the city you want to get the weather for
    city = cityn

    # Make the GET request to the OpenWeatherMap API
    response = requests.get(BASE_URL, params={'q': city, 'appid': API_KEY})

    # Check if the request was successful (status code 200)

    if response.status_code == 200:
    # Parse the JSON response
        weather_data = response.json()
        temp=weather_data['main']['temp']
        if scale=='ce':
            celsiustemp=temp - 273.15

            return {'data' : {
                'city' : weather_data['name'] , 
                'Temperature' : round(celsiustemp,2) , 
                'Scale' : 'Celsius'
                }}
        
        elif scale=='fh':
            fahrentemp=((temp - 273.15) * 9/5 + 32)
            return {'data' : {
            'city' : weather_data['name'], 
            'Temperature' : str(round(fahrentemp, 2)), 
            'Scale' : 'Fahrenheit'
            }}


            