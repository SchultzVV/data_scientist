from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt
from src.tools import generate_dates
import random as rd
import numpy as np
import sys as s
from datetime import datetime
from pandas.tseries.holiday import USFederalHolidayCalendar as calendar

cal = calendar()
holidays = cal.holidays(start=pjme.index.min(), end=pjme.index.max())
# random_y = [int(rd.random()*np.exp(-0.01*i)*150) for i in range(0,len(date_df))]
model = Prophet()

# Adicionar feriados (se necessário)
##holidays = pd.DataFrame({
##    'holiday': 'feriado_nacional',
##    'ds': pd.to_datetime(['2023-01-01', '2023-07-04']),  # Exemplo de feriados
##    'lower_window': 0,
##    'upper_window': 1,
##})


model.add_country_holidays(country_name='US')  # Adicionar feriados dos EUA
model.add_holidays(holidays)

# Adicionar sazonalidades (se necessário)
model.add_seasonality(name='weekly', period=7, fourier_order=3)  # Sazonalidade semanal
model.add_seasonality(name='yearly', period=365, fourier_order=10)  # Sazonalidade anual

#model.fit(df)

# Criar um DataFrame com datas futuras para previsão
future = model.make_future_dataframe(periods=365)  # Prever para 365 dias adicionais

# Fazer previsões
forecast = model.predict(future)

# Plotar previsões
fig = model.plot(forecast)
plt.savefig('forecast_plot.png')