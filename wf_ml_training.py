import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle


def generate_randomForestClassifier(n_estimators, model_name):
    X_train = pd.read_csv("data_processed/X_train.csv")
    X_test = pd.read_csv("data_processed/X_test.csv")
    y_train = pd.read_csv("data_processed/y_train.csv").squeeze()
    y_test = pd.read_csv("data_processed/y_test.csv").squeeze()

    model = RandomForestClassifier(random_state=42, n_estimators=n_estimators)
    model.fit(X_train, y_train)

    with open(f"models/{model_name}", "wb") as file:
        pickle.dump(model, file)
