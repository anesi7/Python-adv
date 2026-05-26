import plotly.express as px

import pandas as pd
import matplotlib.pyplot as pit

df = pd.read_csv("asvIQpercountry.csv")

df['Popullation - 2023']= df['Popullation - 2023'].str.replace(',','').astype(float)

print(df.infol())

fig = px.scatter_geo(df,_locations='Country',locationmode='Country names',
                     over_name='Country', size='Average IQ',color='Continent',
                     projection='natural earth',title='Average IQ by Country',size_max=20,
                     template='plotly_dark')
fig.show()
