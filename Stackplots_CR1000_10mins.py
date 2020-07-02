import plotly.graph_objects as go
import pandas as pd
from datetime import date,timedelta
import plotly.io as pio

# Load data

df = pd.read_csv("CR1000_TenMins.csv",parse_dates=['TIMESTAMP','WS_mph_TMx'] )

print('data read')

#find next midnight
today = date.today()
today1 = date.today()-timedelta(days=3)

# Create figure
fig = go.Figure()

# Add traces


fig.add_trace(go.Scattergl(
   x=list(df.TIMESTAMP), 
    y=list(df.Rain_mm_Tot),
    line={"width": 0.5},
    marker={"size": 2},
    mode="lines+markers",
    name="Rain mm",
    yaxis="y1",
))

fig.add_trace(go.Scattergl(
   x=list(df.TIMESTAMP), 
    y=list(df.Rain_24hr),
    line={"width": 1},
    #marker={"size": 2},
    mode="lines",
    line_shape='hv',
    name="Rain mm",
    yaxis="y8",
))

fig.add_trace(go.Scattergl(
    x=list(df.TIMESTAMP), 
    y=list(df.WS_mph),
    line={"width": 0.5},
    marker={"size": 2},
    mode="lines",
    name="Wind speed mph",
    yaxis="y2",
))

fig.add_trace(go.Scattergl(
    x=list(df.TIMESTAMP), 
    y=list(df.WS_mph_Max),
    line={"width": 0.5},
    marker={"size": 2},
    mode="markers",
    name="Wind speed mph",
    yaxis="y2",
))

fig.add_trace(go.Scattergl(
    x=list(df.TIMESTAMP), 
    y=list(df.WindDir),
    #line={"width": 2},
    marker={"size": 2},
    mode="markers",
    name="Wind Direction",
    yaxis="y3",
))

fig.add_trace(go.Scattergl(
    x=list(df.TIMESTAMP), 
    y=list(df.Temp_air_Avg),
    line={"width": 0.5},
    marker={"size": 2},
    mode="lines+markers",
    name="Air temp",
    yaxis="y4",
))
fig.add_trace(go.Scattergl(
    x=list(df.TIMESTAMP), 
    y=list(df.Temp_soil_Avg),
    line={"width": 0.5},
    marker={"size": 2},
    mode="lines+markers",
    name="Soil Temp",
    yaxis="y9",
))
fig.add_trace(go.Scattergl(
    x=list(df.TIMESTAMP), 
    y=list(df.CO2STP_Avg),
    line={"width": 0.5},
    marker={"size": 2},
    mode="lines+markers",
    name="CO2 soil",
    yaxis="y5",
))
fig.add_trace(go.Scattergl(
    x=list(df.TIMESTAMP), 
    y=list(df.CO2LiSTP_Avg),
    line={"width": 0.5},
    marker={"size": 2},
    mode="lines+markers",
    name="CO2 air",
    yaxis="y6",
))

fig.add_trace(go.Scattergl(
    x=list(df.TIMESTAMP), 
    y=list(df.Pressure_Avg),
    line={"width": 0.5},
    marker={"size": 2},
    mode="lines+markers",
    name="Pressure mb",
    yaxis="y7",
))


# Legend
fig.update_traces(
    #hoverinfo="name+x+text",
    showlegend=False
)

print('added traces')

# Add annotations  deleted block

# Add shapes  deleted block

# Update axes
fig.update_layout(
    xaxis=dict(
        title="Date",
        #autorange=True,
        range=[today1, today],
        type="date",
        showgrid = True,
        gridcolor = "lightgrey",
      	#zeroline = True,
      	showline = True,
      	linecolor="black",
      	#nticks=10,
      	ticks="inside",
      	showticklabels = True,
        
    ),
     yaxis1=dict(
     	title="Rain mm",
        anchor="x",
        autorange=True,
        fixedrange=False,
        domain=[0.0, 0.2],
        linecolor="black",
        mirror=False,
        range=[0,1],
        showline=True,
        side="left",
        #tickfont={"color": "blue"},
        ticks="inside",
        #titlefont={"color": "blue"},
        type="linear",
        showgrid = False,
        zeroline=False
    ),
    yaxis2=dict(
        title="Wind speed",
        anchor="x",
        autorange=True,
        fixedrange=False,
        domain=[0.21, 0.4],
        linecolor="black",
        mirror=True,
        #range=[29.3787777032, 100.621222297],
        showline=True,
        side="right",
        #tickfont={"color": "green"},
        ticks="inside",
        #titlefont={"color": "green"},
        type="linear",
        showgrid = False,
        zeroline=False
    ),
    yaxis3=dict(
        title="Wind direction",
        anchor="x",
        #autorange=True,
        domain=[0.41, 0.6],
        linecolor="black",
        mirror=True,
        range=[0, 361],
        showline=True,
        side="left",
        #tickfont={"color": "orange"},
        ticks="inside",
        dtick=90,
        #titlefont={"color": "orange"},
        type="linear",
        showgrid = True,
        gridcolor="lightgrey",
        zerolinecolor ="lightgrey",
        zeroline= True
    ),
    yaxis4=dict(
        title="Air Temperature",
        anchor="x",
        autorange=True,
        domain=[0.61, 0.8],
        linecolor="black",
        mirror=True,
        #range=[6.63368032236, 8.26631967764],
        showline=True,
        side="right",
        #tickfont={"color": "#607d8b"},
        ticks="inside",
        dtick=5,
        #titlefont={"color": "#607d8b"},
        type="linear",
        showgrid = False,
        zeroline=True,
        zerolinecolor="blue",
        zerolinewidth=0.5,
    ),
     yaxis9=dict(
        title="Soil Temperature",
        anchor="x",
        #autorange=True,
        domain=[0.61, 0.8],
        linecolor="black",
        mirror=True,
        range=[10, 20],
        showline=True,
        side="left",
        #tickfont={"color": "#607d8b"},
        ticks="inside",
        dtick=5,
        #titlefont={"color": "#607d8b"},
        type="linear",
        showgrid = False,
        zeroline=True,
        zerolinecolor="blue",
        zerolinewidth=0.5,
    ),
    
    yaxis5=dict(
        title="CO2 soil ppm",
        anchor="x",
        autorange=True,
        fixedrange=False,
        domain=[0.81, 1],
        linecolor="black",
        mirror=True,
        #range=[380, 480],
        showline=True,
        side="left",
        #tickfont={"color": "#2196F3"},
        ticks="inside",
        #titlefont={"color": "#2196F3"},
        type="linear",
        showgrid = False,
        zeroline=False
    ),
     yaxis6=dict(
        title="CO2 soil air",
        anchor="x",
        autorange=True,
        fixedrange=False,
        domain=[0.81, 1],
        linecolor="black",
        mirror=True,
        #range=[-685.336803224, 3718.33680322],
        showline=True,
        side="right",
        #tickfont={"color": "#2196F3"},
      	ticks="inside",
        #titlefont={"color": "#2196F3"},
        type="linear",
        showgrid = False,
        zeroline=False
    ),
     yaxis7=dict(
        title="Pressure mb",
        anchor="x",
        autorange=True,
        fixedrange=False,
        domain=[0.21,0.4],
        linecolor="black",
        mirror=True,
        #range=[-685.336803224, 3718.33680322],
        showline=True,
        side="left",
        #tickfont={"color": "blue"},
        tickmode="auto",
        ticks="inside",
        #titlefont={"color": "blue"},
        type="linear",
        showgrid = False,
        zeroline=False
    ),
    yaxis8=dict(
        title="Rain cum day",
        #titlefont={"color": "red"},
        anchor="x",
        autorange=True,
        fixedrange=False,
        domain=[0.0,0.2],
        linecolor="black",
        mirror=True,
        #range=[-685.336803224, 3718.33680322],
        showline=True,
        side="right",
        #tickfont={"color": "red"},
        tickmode="auto",
        ticks="inside",
        type="linear",
        showgrid = False,
        zeroline=False
    )    
    
    
        
)


# Update layout
fig.update_layout(
    dragmode="zoom",
    hovermode="x unified",
    legend=dict(traceorder="reversed"),
    height=1000,
    #template="plotly_white",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(
        t=100,
        b=100
    ),
)


# Set title
fig.update_layout(
    title_text="Upper Farringdon Weather"
)

# Add range slider
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1d",
                     step="day",
                     stepmode="backward"),
                dict(count=7,
                     label="1w",
                     step="day",
                     stepmode="backward"),
            	dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

pio.write_html(fig,"plot.html",full_html=False)

#fig.write_html("plot.html", full_html=false)
#fig.show()