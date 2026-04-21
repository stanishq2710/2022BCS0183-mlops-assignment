import mlflow
import mlflow.sklearn
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score

mlflow.set_tracking_uri("file:./mlruns")
mlflow.set_experiment("2022BCS0183_experiment")

def load_data():
    df = pd.read_csv("data/dataset.csv")
    X = df.drop("species", axis=1)
    y = df["species"]
    return train_test_split(X, y, test_size=0.2, random_state=42)

def run_experiment(model_type="rf", n_estimators=100, feature_subset=None):
    X_train, X_test, y_train, y_test = load_data()

    # Feature selection
    if feature_subset:
        X_train = X_train[feature_subset]
        X_test = X_test[feature_subset]

    # Model selection
    if model_type == "rf":
        model = RandomForestClassifier(n_estimators=n_estimators)
    else:
        model = LogisticRegression(max_iter=200)

    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)
    f1 = f1_score(y_test, preds, average="macro")

    with mlflow.start_run():
        mlflow.log_param("model", model_type)
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("features", str(feature_subset))

        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("f1_score", f1)

        mlflow.sklearn.log_model(model, "model")
        joblib.dump(model, "model.pkl")

        print(f"Run completed → Acc: {acc}, F1: {f1}")

if __name__ == "__main__":
    # Run 1: Base
    run_experiment("rf", 100)

    # Run 2: Hyperparameter change
    run_experiment("rf", 200)

    # Run 3: Same model, different dataset already handled via DVC

    # Run 4: Feature selection
    run_experiment("rf", 100, ["sepal_length", "petal_length"])

    # Run 5: Different model
    run_experiment("lr")
