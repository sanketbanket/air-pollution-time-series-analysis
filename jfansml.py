import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels as ss
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

df = pd.read_csv('F:\\dev_stuff\\DSP_TIME_SERIES\\air+quality\\AirQualityUCI.csv',sep = ';')

# Combine the Date and Time columns into a single datetime column
df['datetime'] = df['Date'] + ' ' + df['Time']

# Ensure the datetime column is set as the index




print(df)
# Plot the time series for PT08.S1(CO)
plt.figure(figsize=(12, 6))

some_data = [float(x.replace(',', '.')) for x in df["C6H6(GT)"].to_list()]
plt.plot(some_data, label='C6H6', color='blue')

# Add labels and title
plt.xlabel('Date')
plt.ylabel('C6H6 Concentration ')
plt.title('Time Series of C6H6 Concentration')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Add a legend
plt.legend()

plt.show()


plot_acf(some_data, lags = 50)
plt.show()


