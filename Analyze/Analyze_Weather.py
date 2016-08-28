from US_State_Choropleth import State_Choropleth
from datetime import *


"""This class analyzes parses weather data in a variety of ways."""
class Weather_Analysis():
    def __init__(self):
        self.start_time = datetime.now()


    def analyze(self):
        state_map = State_Choropleth()
        state_map.plotFigure()
        self.updateRuntime()


    def updateRuntime(self):
        end_time = datetime.now()
        runtime = end_time - self.start_time
        print runtime


Analysis = Weather_Analysis()
Analysis.analyze()


