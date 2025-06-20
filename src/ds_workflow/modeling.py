from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


def benchmark_models(X, y):
    """Retorna as médias de acurácia de modelos simples."""
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    lr = LogisticRegression(max_iter=1000)
    rf = RandomForestClassifier(random_state=42)
    lr_score = cross_val_score(lr, X_scaled, y, cv=5).mean()
    rf_score = cross_val_score(rf, X, y, cv=5).mean()
    return {"logistic_regression": lr_score, "random_forest": rf_score}
