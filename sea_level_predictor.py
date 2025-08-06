import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the data
df = pd.read_csv('epa-sea-level.csv')


plt.figure(figsize=(10,6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])


# Linear regression for full dataset
res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
years_extended = pd.Series(range(1880, 2051))
plt.plot(
    years_extended, 
    res.intercept + res.slope*years_extended, 
    label='Best fit line (1880-2050)', 
    color='r'
)


df_recent = df[df['Year'] >= 2000]
res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
years_recent_extended = pd.Series(range(2000, 2051))
plt.plot(
    years_recent_extended, 
    res_recent.intercept + res_recent.slope*years_recent_extended, 
    label='Best fit line (2000-2050)', 
    color='g'
)

plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()
plt.tight_layout()
# plt.savefig('sea_level_plot.png')  # If needed for export
return plt.gcf()
