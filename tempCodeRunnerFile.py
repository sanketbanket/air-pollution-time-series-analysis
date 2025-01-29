m = Prophet()
m.fit(c6h6)  # df is a pandas.DataFrame with 'y' and 'ds' columns
future = m.make_future_dataframe(periods=365)
m.predict(future)
