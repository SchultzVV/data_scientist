from prophet import Prophet
import pandas as pd
import matplotlib.pyplot as plt
from src.tools import generate_dates
import random as rd
import numpy as np
import sys as s
from datetime import datetime

data = {
    'ds': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04'],
    'y': [100, 120, 95, 105]
}
def generate_data(size):
    start_date = datetime(2023, 1, 1)  # Data inicial
    num_days = size
    date_df = generate_dates(start_date, num_days)
    random_y = [int(rd.random()*np.exp(-0.01*i)*150) for i in range(0,len(date_df))]
    
    # random_y = np.linspace(0,num_days,num_days)
    #random_y = [np.cos(o) for o in random_y]
    data = {
        'ds': date_df,
        'y': random_y
    }
    df = pd.DataFrame(data)
    return df
df = generate_data(200)
print(df)
print(type(df))
# s.exit()


model = Prophet()

model.add_country_holidays(country_name='US')  # Exemplo de adição de feriados dos EUA
model.fit(df)
future = model.make_future_dataframe(periods=4)  # Prever para 365 dias adicionais
forecast = model.predict(future)
fig = model.plot(forecast)
components = model.plot_components(forecast)
#model = Prophet(growth='logistic', seasonality_prior_scale=0.1)

#future = model.make_future_dataframe(periods=365)  # Prever para 365 dias adicionais

# Fazer previsões
forecast = model.predict(future)

# Plotar previsões
fig = model.plot(forecast)
plt.savefig('forecast_plot.png')