from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\jatin\\OneDrive\\Desktop\\yug_some\\air-pollution-time-series-analysis\\AirQualityUCI.csv',sep = ';')

# Combine the Date and Time columns into a single datetime column

df['datetime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format="%d/%m/%Y %H.%M.%S")


c6h6 = [float(x.replace(',', '.')) for x in df["C6H6(GT)"].to_list()]


data = {
    'ds': df['datetime'],
    'y' : c6h6
}
data = pd.DataFrame(data)
data['ds'] = pd.to_datetime(data['ds'])


m = Prophet(daily_seasonality=True)
m.fit(data)  # df is a pandas.DataFrame with 'y' and 'ds' columns
future = m.make_future_dataframe(periods=10)
forecast = m.predict(future)

print()

'''m.plot(forecast)
plt.show()'''

