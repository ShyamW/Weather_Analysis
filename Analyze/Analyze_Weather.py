import plotly.plotly as py


py.sign_in('gingerbread123', '5wi0st6l25')


scl = [[0.0, 'rgb(242,240,247)'], [0.2, 'rgb(218,218,235)'], [0.4, 'rgb(188,189,220)'],  [0.6, 'rgb(158,154,200)'],
       [0.8, 'rgb(117,107,177)'], [1.0, 'rgb(84,39,143)']]



def formStateWeatherDict():
    state_to_temp = dict()
    with open('../DATA/DATA_OUT/weather_out') as f:
        for weather in f:
            try:
                if '*' not in weather:
                    weather = weather.strip('\n').split(',')
                    temperature = int(weather[5].replace('Temperature: ','').replace(' ',''))
                    state = weather[8].split(' ')[-1]
                    print temperature
                    print state
                    if state in state_to_temp.keys():
                        state_to_temp[state].append(temperature)
                    else:
                        state_to_temp[state] = [temperature]
            except: pass
    return state_to_temp


def calculateAvgTemp(state_to_temp):
    for state, temperatures in state_to_temp.items():
        avg_temp = sum(temperatures) / float(len(temperatures))
        state_to_temp[state] = avg_temp


state_to_temp = formStateWeatherDict()
calculateAvgTemp(state_to_temp)


data = [dict(
        type='choropleth',
        colorscale=scl,
        autocolorscale=False,
        locations=state_to_temp.keys(),
        z=state_to_temp.values(),
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

layout = dict(
        title='Average Temperature by State<br>(Hover for breakdown)',
        geo=dict(
            scope='usa',
            projection=dict(type='albers usa'),
            showlakes=True,
            lakecolor='rgb(255, 255, 255)',
        ),
    )

fig = dict(data=data, layout=layout)

url = py.plot(fig, filename='US Temperatures')