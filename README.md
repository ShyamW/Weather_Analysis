# Weather Analysis Documentation
This repository serves two functions:
  1. Gather Temperature data for US cities
  2. Calculate Average Temperatures of each US state
 
## Gather Temperature Data for US cities
This module (located under Get_Weather_Data) requests weather data from the national weather service for each US city. Weather data (such as temperature, forecasts, and change of precipitation) and location data (such as location coordinates, and states) are recorded in a data txt file.

Since parsing weather data for all US cities is relatively slow, past forecast data is recorded in the data txt file. 

If you wish to parse current weather data, ensure the following requirements are met.

##### Parsing Requirements
1. Python

