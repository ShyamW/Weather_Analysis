import plotly.plotly as py

"""This class Takes National Weather Data gathered from Weather.gov and outputs a US state choropleth of average
state temperatures."""

class Choropleth():
    def __init__(self):
        self.scale = [[]]
        self.state_to_temp = dict()
        self.data = dict()
        self.layout = dict()


    """Sets the color scale for the choropleth map"""
    def setScale(self):
        self.scl = [[0.0, 'rgb(242,240,247)'], [0.2, 'rgb(218,218,235)'], [0.4, 'rgb(188,189,220)'],
                    [0.6, 'rgb(158,154,200)'], [0.8, 'rgb(117,107,177)'], [1.0, 'rgb(84,39,143)']]


    """Signs in to Plotly"""
    def signIn(self):
        py.sign_in('gingerbread123', '5wi0st6l25')


    """Forms a dictionary of {state: [temperatures]} by reading weather dat from weather_out.
    @updates self.state_to_temp
        adds temperatures read from file"""
    def formStateWeatherDict(self):
        with open('../DATA/DATA_OUT/weather_out') as f:
            for weather in f:
                try:
                    if '*' not in weather:
                        weather = weather.strip('\n').split(',')
                        temperature = int(weather[5].replace('Temperature: ', '').replace(' ', ''))
                        state = weather[8].split(' ')[-1]
                        if state in self.state_to_temp.keys():
                            self.state_to_temp[state].append(temperature)
                        else:
                            self.state_to_temp[state] = [temperature]
                except:
                    pass


    """Updates the value temperature with the average of all temperatures recorded in the state
    @updates state_to_temp"""
    def calculateAvgTemp(self):
        for state, temperatures in self.state_to_temp.items():
            avg_temp = sum(temperatures) / float(len(temperatures))
            self.state_to_temp[state] = avg_temp


    """Builds the Configuration JSON for the Choropleth Plot.
    @replaces self.data"""
    def FormPlotJSON(self):
        self.data = [dict(
            type='choropleth',
            colorscale=self.scl,
            autocolorscale=False,
            locations=self.state_to_temp.keys(),
            z=self.state_to_temp.values(),
            locationmode='USA-states',
            text='temperature is',
            marker=dict(
                line=dict(
                    color='rgb(255,255,255)',
                    width=2
                )
            ),
            colorbar=dict(
                title="Temperature (Fahrenheit)"
            )
        )]
        self.layout = dict(
            title='Average Temperature by State<br>(Hover for breakdown)',
            geo=dict(
                scope='usa',
                projection=dict(type='albers usa'),
                showlakes=True,
                lakecolor='rgb(255, 255, 255)'
            )
        )


    """Plots the state temperature map on plotly's website."""
    def showPlot(self):
        fig = dict(data=self.data, layout=self.layout)
        url = py.plot(fig, filename='US Temperatures')
        print url


    """Performs all tasks needed to produce a choropleth."""
    def plotFigure(self):
        self.signIn()
        self.setScale()
        self.formStateWeatherDict()
        self.calculateAvgTemp()
        self.FormPlotJSON()
        self.showPlot()


Choropleth = Choropleth()
Choropleth.plotFigure()
