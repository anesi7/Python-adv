import matplotlib.pyplot as plt
from matplotlib import
import pandas as pd

df = pd.read_csv('avgIQpercountry.csv')

avg_iq_by_continent = df.grupby('Comtinent')["Average IQ"].mean()

plt.figure(figsize=(10,6))

avg_iq_by_continent.plot(kind='line',maker='o',color='skyblue')


plt.show()