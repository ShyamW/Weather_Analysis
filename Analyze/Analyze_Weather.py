import plotly.plotly as py


py.sign_in('gingerbread123', '5wi0st6l25')


scl = [[0.0, 'rgb(242,240,247)'], [0.2, 'rgb(218,218,235)'], [0.4, 'rgb(188,189,220)'],  [0.6, 'rgb(158,154,200)'],
       [0.8, 'rgb(117,107,177)'], [1.0, 'rgb(84,39,143)']]

states = []
with open('../Weather_Analysis/DATA/DATA_IN/STATES.txt') as f:
    for state in f:
        states.append(state.strip('\n'))


a = []
for i in range(51):
    a.append(i)
data = [dict(
        type='choropleth',
        colorscale=scl,
        autocolorscale=False,
        locations=states,
        z=a,
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

url = py.plot(fig, filename='d3-cloropleth-map')