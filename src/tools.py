from datetime import datetime, timedelta
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly


def load_data(filename):
    if filename == None:
        filename = 'MaunaLoaDailyTemps.csv'
    df = pd.read_csv(filename)
    return df

def treat_df(df):
    df.dropna(inplace= True)
    df.reset_index(drop=True, inplace=True)
    df=df[["DATE","AvgTemp"]]
    df.columns = ['ds','y']
    df['ds'] = pd.to_datetime(df['ds'])
    return df

def plot_df(df):
    df.plot(x='ds',y='y',figsize=(18,6))

def train_test_split(df):
    train = df.iloc[:len(df)-365]
    test = df.iloc[len(df)-365:]
    return train, test

def fit_model(data):
    m = Prophet()
    return m.fit(data)

def get_furute(m, periods):
    future = m.make_future_dataframe(periods=periods) #MS for monthly, H for hourly
    forecast = m.predict(future)
    return future

def predict(m, future):
    forecast = m.predict(future)
    forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
    return forecast

def plot_forecast(m ,forecast):
    plot_plotly(m ,forecast)
    

def generate_dates(start_date, num_days):
    date_list = [start_date + timedelta(days=i) for i in range(num_days)]
    date_list = [start_date + timedelta(days=i) for i in range(num_days)]
    formatted_dates = [date.strftime('%Y-%m-%d') for date in date_list]
    # return pd.DataFrame({'ds': date_list})
    return formatted_dates


# Exemplo de uso da função para gerar datas consecutivas para 5000 dias a partir de uma data inicial

def main():
    start_date = datetime(2023, 1, 1)  # Data inicial
    num_days = 5000
    date_df = generate_dates(start_date, num_days)

    # Visualizando as datas geradas
    print(date_df)

if __name__ == "__main__":
    main()    
