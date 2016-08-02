import ConfigParser
from bs4 import BeautifulSoup as HTML
def getURL():
    config = ConfigParser.ConfigParser()
    config.read('CONFIG.ini')
    url = (config.get('URL', 'Knoxville'))
    print url
    return url


def getWeather(url):
    


def main():
    url = getURL()
    getWeather(url)