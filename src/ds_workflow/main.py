from . import eda, modeling, feature_store, mlflow_utils, deploy


def run_workflow():
    df = eda.load_wine_dataset()
    eda.run_basic_eda(df)
    p_value = eda.check_normality(df["alcohol"])
    print("p-value normalidade:", p_value)

    X = df.drop("target", axis=1)
    y = df["target"]
    scores = modeling.benchmark_models(X, y)
    print("Benchmark:", scores)

    pipeline = feature_store.build_feature_pipeline()
    X_feat = pipeline.fit_transform(X, y)
    feature_store.save_features(X_feat)

    # Usa modelo mais simples para log no MLflow
    from sklearn.linear_model import LogisticRegression
    acc = mlflow_utils.log_run(LogisticRegression(max_iter=1000), X_feat, y)
    print("Acurácia registrada:", acc)

    current = scores["logistic_regression"]
    candidate = current - 0.05
    current, ok = deploy.simulate_canary(current, candidate)
    if not ok:
        candidate = current + 0.03
        current, _ = deploy.simulate_canary(current, candidate)


if __name__ == "__main__":
    run_workflow()
