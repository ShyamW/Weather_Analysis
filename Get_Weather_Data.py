import ConfigParser
from bs4 import BeautifulSoup as HTML
import urllib2
from Weather_Forecast import Weather_Forecast



"""Gets all Coordinates to determine weather for
@return lat_lng
    Dictionary of lat: lng"""
def getAllCoordinates():
    lat_lng = {}
    with open('lat_lng') as city_data_file:
        for city_data in city_data_file:
            city_data = city_data.split(',')
            state = city_data[1]
            city = city_data[2]
            print city + ', ' + state
            lat = city_data[3]
            lng = city_data[4].strip('\n')
            lat_lng[lat] = lng
    return lat_lng


"""Gets base url to parse
@param lat
    latitude to replace into url
@param lng
    Longitude to replace into url"""
def getURL(lat, lng):
    config = ConfigParser.ConfigParser()
    config.read('CONFIG.ini')
    url = (config.get('URL', 'Knoxville'))
    url = str(url).replace('lat', str(lat)).replace('lng', str(lng))
    return url


"""Gets Weather Information and Writes data to file.
@param url
    url to parse weather for
@param lat
    latitude of weather forecast
@param lng
    longitude of weather forecast"""
def getWeather(url, lat, lng):
    weather_data = HTML(urllib2.urlopen(url).read(), 'lxml')
    # Navigate down HTML to the weather table (line 410 generally)
    try:
        weather_table = weather_data.body.contents[5].contents[5].contents[22].contents[5].contents[5].table
        weather_forecast = Weather_Forecast(lat, lng)
        weather_forecast.detWeatherProperties(weather_table)
        weather_forecast.outputWeatherProperties()
        print url
    except:
        print 'url down'


"""Main Method"""
def main():
    lat_lng = getAllCoordinates()
    for lat, lng in lat_lng.items():
        url = getURL(lat,lng)
        getWeather(url, lat, lng)


if __name__ == '__main__':
    main()