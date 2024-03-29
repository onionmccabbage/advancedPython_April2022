import requests

class WeatherGetter:
    def __init__(self, city='plymouth', country='uk'):
        self.city    = city
        self.country = country
        self.APIkey  = 'APPID=48f2d5e18b0d2bc50519b58cce6409f1'

    def getWeather(self):
        url_str = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&{}'
        url = url_str.format(self.city, self.country, self.APIkey)
        response = requests.get(url)
        data  = response.json()
        if 'main' in data:
            return data  

if __name__ == '__main__':
    pass