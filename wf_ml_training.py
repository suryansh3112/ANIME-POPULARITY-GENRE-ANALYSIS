import pandas as pd
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
import pickle

RANDOM_STATE = 17


def generate_randomForestClassifier(
    model_name, n_estimators, max_depth=None, min_samples_leaf=1, criterion="gini"
):
    X_train = pd.read_csv("data_processed/X_train.csv")
    y_train = pd.read_csv("data_processed/y_train.csv").squeeze()

    model = RandomForestClassifier(
        random_state=RANDOM_STATE,
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_leaf=min_samples_leaf,
        criterion=criterion,
    )
    model.fit(X_train, y_train)

    with open(f"models/{model_name}", "wb") as file:
        pickle.dump(model, file)


def generate_GradientBoostingClassifier(model_name):
    X_train = pd.read_csv("data_processed/X_train.csv")
    y_train = pd.read_csv("data_processed/y_train.csv").squeeze()
    model = GradientBoostingClassifier(random_state=RANDOM_STATE)
    model.fit(X_train, y_train)
    with open(f"models/{model_name}", "wb") as file:
        pickle.dump(model, file)


def generate_LogisticRegressionModel(model_name):
    X_train = pd.read_csv("data_processed/X_train.csv")
    y_train = pd.read_csv("data_processed/y_train.csv").squeeze()
    model = LogisticRegression(random_state=RANDOM_STATE, max_iter=1000)
    model.fit(X_train, y_train)
    with open(f"models/{model_name}", "wb") as file:
        pickle.dump(model, file)
