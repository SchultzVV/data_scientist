import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif


def build_feature_pipeline(k=8):
    """Cria pipeline de transformação e seleção de features."""
    return Pipeline([
        ("scale", StandardScaler()),
        ("select", SelectKBest(score_func=f_classif, k=k)),
    ])


def save_features(X_transformed, path="feature_store.csv"):
    pd.DataFrame(X_transformed).to_csv(path, index=False)
