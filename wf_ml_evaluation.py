import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, MultiLabelBinarizer
import pickle, ast
from wf_ml_training import (
    generate_randomForestClassifier,
    generate_GradientBoostingClassifier,
    generate_LogisticRegressionModel,
)
from sklearn.metrics import accuracy_score, f1_score
from wf_ml_prediction import get_prediction
from wf_ml_prediction import predict

RANDOM_FOREST_100 = "random_forest_model_100.pkl"
RANDOM_FOREST_200 = "random_forest_model_200.pkl"
GRADIENT_BOOSTING_CLASSIFIER = "gradient_boosting_classifier.pkl"
LOGISTIC_REGRESSION_MODEL = "logistic_regression_model.pkl"


def save_training_and_testing_data():
    data = pd.read_csv("data_processed/anime_processed_data.csv")

    selected_features = [
        "Source",
        "Episodes",
        "Rating",
        "Season",
        "Year",
        "Broadcast_Day",
        "Producers",
        "Licensors",
        "Studios",
        "Genres",
        "Themes",
    ]

    data = data[selected_features + ["Score", "Type"]]

    single_label_categorical = ["Source", "Rating", "Season", "Broadcast_Day"]

    multi_label_categorical = ["Producers", "Licensors", "Studios", "Genres", "Themes"]

    score_median = data["Score"].median()
    data["Popularity_Output"] = data["Score"].apply(
        lambda x: 1 if x > score_median else 0
    )
    data = data.drop(columns=["Score"])

    scaler_episodes = MinMaxScaler()
    data["Episodes"] = scaler_episodes.fit_transform(data[["Episodes"]])

    scaler_year = MinMaxScaler()
    data["Year"] = scaler_year.fit_transform(data[["Year"]])

    with open("models/scaler_episodes.pkl", "wb") as f:
        pickle.dump(scaler_episodes, f)

    with open("models/scaler_year.pkl", "wb") as f:
        pickle.dump(scaler_year, f)

    factorize_mappings = {}
    for feature in single_label_categorical:
        data[feature], uniques = pd.factorize(data[feature])
        factorize_mappings[feature] = dict(zip(uniques, range(len(uniques))))

    with open("models/factorize_mappings.pkl", "wb") as f:
        pickle.dump(factorize_mappings, f)

    mlb_dict = {}
    for feature in multi_label_categorical:
        data[feature] = data[feature].apply(
            lambda x: ast.literal_eval(x) if isinstance(x, str) and x != "nan" else []
        )
        mlb = MultiLabelBinarizer()
        transformed_data = mlb.fit_transform(data[feature])
        transformed_df = pd.DataFrame(
            transformed_data, columns=[f"{feature}_{label}" for label in mlb.classes_]
        )
        data = pd.concat([data.drop(columns=[feature]), transformed_df], axis=1)
        mlb_dict[feature] = mlb

    with open("models/mlb_dict.pkl", "wb") as f:
        pickle.dump(mlb_dict, f)

    data = data[data["Type"].isin(["TV"])]

    data = data.drop(columns=["Type"])

    X = data.drop(columns=["Popularity_Output"])
    y = data["Popularity_Output"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=40, stratify=y
    )

    X_train.to_csv("data_processed/X_train.csv", index=False)
    X_test.to_csv("data_processed/X_test.csv", index=False)
    y_train.to_csv("data_processed/y_train.csv", index=False)
    y_test.to_csv("data_processed/y_test.csv", index=False)

    # print("Training data shape:", X_train.shape)
    # print("Test data shape:", X_test.shape)
    # print("yTraining data shape:", y_train.shape)
    # print("yTest data shape:", y_test.shape)
    # print("y_train distribution:\n", y_train.value_counts(normalize=True))
    # print("y_test distribution:\n", y_test.value_counts(normalize=True))


def save_metrics(model_name, mode="a"):
    X_test = pd.read_csv("data_processed/X_test.csv")
    y_test = pd.read_csv("data_processed/y_test.csv").squeeze()
    with open(f"models/{model_name}", "rb") as file:
        model = pickle.load(file)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    with open("evaluation/summary.txt", mode) as f:
        f.write(f"Model: {model_name}\n")
        f.write(f"Accuracy: {accuracy*100:.4f}%\n")
        f.write(f"F1-Score: {f1:.4f}\n\n")


def test_feature_impact(model_name):
    source_values = [
        "Manga",
        "Visual novel",
        "Original",
        "Game",
        "Mixed media",
        "Other",
    ]
    studio_values = [
        "Bones",
        "Madhouse",
        "Pierrot Films",
        "DRAWIZ",
        "Kigumi",
        "RAMS",
    ]
    for source in source_values:
        df = pd.DataFrame(
            {
                "Source": [source],
                "Episodes": [12],
                "Rating": ["PG-13 - Teens 13 or older"],
                "Season": ["fall"],
                "Year": [2018],
                "Broadcast_Day": ["Wednesdays"],
                "Producers": ["Aniplex"],
                "Licensors": ["Funimation"],
                "Studios": ["DRAWIZ"],
                "Genres": ["Action, Adventure"],
                "Themes": ["Military"],
            }
        )
        prediction = predict(df, model_name)
        print(f"Source: {source} -> Prediction: {prediction}")
    print()
    for studio in studio_values:
        df = pd.DataFrame(
            {
                "Source": ["Other"],
                "Episodes": [12],
                "Rating": ["PG-13 - Teens 13 or older"],
                "Season": ["fall"],
                "Year": [2018],
                "Broadcast_Day": ["Wednesdays"],
                "Producers": ["Aniplex"],
                "Licensors": ["Funimation"],
                "Studios": [studio],
                "Genres": ["Action, Adventure"],
                "Themes": ["Military"],
            }
        )
        prediction = predict(df, model_name)
        print(f"Studio: {studio} -> Prediction: {prediction}")
    print()
    for source in source_values:
        for studio in studio_values:
            df = pd.DataFrame(
                {
                    "Source": [source],
                    "Episodes": [12],
                    "Rating": ["PG-13 - Teens 13 or older"],
                    "Season": ["fall"],
                    "Year": [2018],
                    "Broadcast_Day": ["Wednesdays"],
                    "Producers": ["Aniplex"],
                    "Licensors": ["Funimation"],
                    "Studios": [studio],
                    "Genres": ["Action, Adventure"],
                    "Themes": ["Military"],
                }
            )
            prediction = predict(df, model_name)
            print(f"Source: {source}, Studios: {studio} -> Prediction: {prediction}")


# Saving testing and training data
save_training_and_testing_data()

# Model 1
generate_randomForestClassifier(
    model_name=RANDOM_FOREST_100, n_estimators=100, criterion="entropy"
)
save_metrics(RANDOM_FOREST_100, "w")
get_prediction(RANDOM_FOREST_100)

# Model 2
generate_randomForestClassifier(model_name=RANDOM_FOREST_200, n_estimators=200)
save_metrics(RANDOM_FOREST_200)
get_prediction(RANDOM_FOREST_200)

# Model 3
generate_GradientBoostingClassifier(GRADIENT_BOOSTING_CLASSIFIER)
save_metrics(GRADIENT_BOOSTING_CLASSIFIER)
get_prediction(GRADIENT_BOOSTING_CLASSIFIER)

# Model 4
generate_LogisticRegressionModel(LOGISTIC_REGRESSION_MODEL)
save_metrics(LOGISTIC_REGRESSION_MODEL)
get_prediction(LOGISTIC_REGRESSION_MODEL)

# Testing feature impact
# test_feature_impact(RANDOM_FOREST_100)
