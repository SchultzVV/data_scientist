import mlflow


def log_run(model, X, y, experiment="wine_demo"):
    mlflow.set_experiment(experiment)
    with mlflow.start_run():
        model.fit(X, y)
        acc = model.score(X, y)
        mlflow.log_metric("accuracy", acc)
        mlflow.sklearn.log_model(model, "model")
    return acc
