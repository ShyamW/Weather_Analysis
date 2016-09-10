# Weather Analysis Documentation
This repository serves two functions:
  1. Gather Temperature data for US cities
  2. Plot Average Temperatures of each US state on a US Choropleth Diagram
 
## Gather Temperature Data for US cities
This module (located under Get_Weather_Data) requests weather data from the national weather service for each US city. Weather data (such as temperature, forecasts, and change of precipitation) and location data (such as location coordinates, and states) are recorded in a data txt file.

Since parsing weather data for all US cities is relatively slow, past forecast data is recorded in the data txt file. 

To parse current weather data, ensure the following requirements are met.

##### Parsing Requirements
1. Python 2.7 or Later
    * Programming Language
2. ConfigParser (configparser if python 3.x)
    * Library to read parameter data such as the url to parse
3. requests 
    * Used to Parse Weather Data from National Weather Service   
4. bs4
    * Used to Parse forecast data in XML format
5. lxml
    * XML parser used by bs4

## Form a US State Choropleth Diagram of Average temperatures
This module analyzes parsed weather data by creating a dictionary of states to reported temperatures. Temperatures are then averaged for each state and then plotted using plotly's chorpleth api.

To analyze and plot parsed weather data, ensure the following requirements are met.

##### Parsing Requirements
1. Python 2.7 or Later
    * Programming Language
2. Plotly 
    * Library used to form a state temperature choropleth
2. ConfigParser (configparser if python 3.x)
    * Library to read parameter data such as the url to parse

