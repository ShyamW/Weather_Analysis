import ConfigParser
from bs4 import BeautifulSoup as HTML
import urllib2
from Weather_Forecast import Weather_Forecast

def getURL(lat, lng):
    config = ConfigParser.ConfigParser()
    config.read('CONFIG.ini')
    url = (config.get('URL', 'Knoxville'))
    url = str(url).replace('lat', str(lat)).replace('lng', str(lng))
    print url
    return url


def getWeather(url, lat, lng):
    weather_data = HTML(urllib2.urlopen(url).read(), 'lxml')
    # Navigate down HTML to the weather table (line 410 generally)
    weather_table = weather_data.body.contents[5].contents[5].contents[22].contents[5].contents[5].table
    weather_forecast = Weather_Forecast(lat, lng)
    weather_forecast.detWeatherProperties(weather_table)
    weather_forecast.outputWeatherProperties()



def main():
    lat = 35
    lng = -90
    for i in range(20):
        url = getURL(lat,lng)
        getWeather(url, lat, lng)
        lat+=.1
        lng-=.1


if __name__ == '__main__':
    main()