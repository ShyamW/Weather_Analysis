# Weather Analysis Documentation
This repository serves two functions:
  1. Gather Temperature data for US cities
  2. Plot Average Temperatures of each US state on a Choropleth Diagram
  
**Screen Cap**
![alt tag](https://raw.githubusercontent.com/shyamw/Weather_Analysis/master/Documentation/Capture.PNG)

## 1. Gather Temperature Data for US cities
This module (located under Get_Weather_Data) requests weather data from the national weather service for each US city. Weather data (such as temperature, forecasts, and change of precipitation) and location data (such as location coordinates, and states) are recorded in a data txt file.

Since parsing weather data for all US cities is relatively slow, past forecast data is recorded in the data txt file. 

To parse current weather data, ensure the following requirements are met.

## 2. Form a US State Choropleth Diagram of Average temperatures
This module analyzes parsed weather data by creating a dictionary of states to reported temperatures. Temperatures are then averaged for each state and then plotted using plotly's chorpleth api.

To analyze and plot parsed weather data, ensure the requirements below are met.


## Basic Requirements
1. [Python 2.X](https://www.python.org/downloads/)
    * Python 2.7 recommended

	        sudo apt-get install python
      
2. [ConfigParser](https://pypi.python.org/pypi/configparser)
   * Used to Read API Key information
   
	        pip install ConfigParser
    
## Parsing Requirements
4. [requests](http://docs.python-requests.org/en/master/)
   * Used to Parse Weather Data from National Weather Service
   
            pip install requests
	  
5. [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
   * Used to Parse forecast data in XML format
   
          pip install bs4
	  
6. [lxml](http://lxml.de/index.html#download)
   * XML parser used by bs4
   
          pip install lxml
    
## Plotting Requirements
1. [plotly](https://plot.ly/python/getting-started/)
   * Library used to form a state temperature choropleth
   
          pip install plotly

