from datetime import datetime, timedelta
import pandas as pd

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
