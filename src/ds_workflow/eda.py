import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


def load_wine_dataset():
    """Carrega o dataset Wine do scikit-learn como DataFrame."""
    from sklearn.datasets import load_wine
    data = load_wine()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    return df


def run_basic_eda(df):
    """Executa inspeções e visualizações básicas."""
    stats_desc = df.describe()
    corr = df.corr()
    sns.heatmap(corr, cmap="coolwarm")
    plt.close()  # evita abrir janelas interativas
    return stats_desc, corr


def check_normality(series):
    """Retorna o p-valor do teste de normalidade de D'Agostino."""
    _, p = stats.normaltest(series)
    return p
