import pandas as pd
import numpy as np
import plotly.express as px

# ----- Step 1: Create Sample Data -----
data = {
    'Country': ['Afghanistan', 'United States', 'China', 'India', 'Germany', 'Brazil', 
                'Japan', 'Canada', 'Australia', 'Nigeria', 'France', 'United Kingdom', 
                'South Africa', 'Mexico', 'Kenya', 'Russia', 'Italy', 'Indonesia', 
                'Turkey', 'Saudi Arabia', 'Spain', 'South Korea', 'Argentina'],
    'ISO_code': ['AFG', 'USA', 'CHN', 'IND', 'DEU', 'BRA', 'JPN', 'CAN', 'AUS', 'NGA', 
                'FRA', 'GBR', 'ZAF', 'MEX', 'KEN', 'RUS', 'ITA', 'IDN', 'TUR', 'SAU', 
                'ESP', 'KOR', 'ARG'],
    'GDP_per_capita_2010': [503.6, 48466.8, 4550.5, 1357.6, 41785.6, 11286.2, 44507.7, 
                           47447.5, 51850.0, 2327.3, 40638.3, 39436.6, 7329.0, 9271.4, 
                           967.0, 10675.0, 35849.4, 3122.4, 10672.6, 19259.6, 30736.6, 
                           22087.0, 10385.9],
    'GDP_per_capita_2015': [543.8, 56839.4, 8066.9, 1605.6, 41219.1, 8814.0, 34524.5, 
                           43525.4, 56554.3, 2730.4, 36526.8, 44305.5, 5734.6, 9143.1, 
                           1355.0, 9313.0, 30180.3, 3336.2, 10984.9, 20628.4, 25683.8, 
                           27105.1, 12654.4],
    'GDP_per_capita_2021': [469.9, 69287.5, 12556.3, 2256.6, 51203.6, 7518.8, 39312.7, 
                           51987.9, 62619.0, 2065.7, 43518.5, 47334.4, 6994.2, 10045.7, 
                           2006.8, 12194.8, 35551.3, 4291.4, 9586.6, 23185.7, 30103.5, 
                           34997.8, 10636.1]
}

df = pd.DataFrame(data)

# ----- Step 2: Reshape Data for Animation -----
gdp_df = pd.melt(
    df,
    id_vars=['Country', 'ISO_code'],
    value_vars=['GDP_per_capita_2010', 'GDP_per_capita_2015', 'GDP_per_capita_2021'],
    var_name='Year',
    value_name='GDP_per_capita'
)
gdp_df['Year'] = gdp_df['Year'].str.extract(r'(\d+)').astype(int)

# ----- Step 3: Create Animated Choropleth -----
fig = px.choropleth(
    gdp_df,
    locations='ISO_code',
    color='GDP_per_capita',
    hover_name='Country',
    animation_frame='Year',
    color_continuous_scale='RdYlGn',  # Red = low, Green = high
    projection='natural earth',
    title='GDP per Capita by Country (2010-2021)',
    labels={'GDP_per_capita': 'GDP per Capita (USD)'},
    hover_data={'ISO_code': False}
)

# ----- Step 4: Add Country Borders and Layout Tweaks -----
fig.update_traces(marker_line_width=0.5, marker_line_color='black')  # borders on countries
fig.update_layout(
    coloraxis_colorbar=dict(
        title='GDP per Capita (USD)',
        tickprefix='$'
    ),
    margin=dict(l=0, r=0, t=50, b=0),
    height=800,
    width=1400
)

fig.show()
