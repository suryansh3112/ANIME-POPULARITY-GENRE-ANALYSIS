import pickle
import pandas as pd


def get_formatted_input(new_input):
    with open("models/scaler_episodes.pkl", "rb") as f:
        scaler_episodes = pickle.load(f)

    with open("models/scaler_year.pkl", "rb") as f:
        scaler_year = pickle.load(f)

    with open("models/mlb_dict.pkl", "rb") as f:
        mlb_dict = pickle.load(f)

    with open("models/factorize_mappings.pkl", "rb") as f:
        factorize_mappings = pickle.load(f)

    for feature, mapping in factorize_mappings.items():
        new_input[feature] = new_input[feature].map(mapping).fillna(-1).astype(int)

    for feature in mlb_dict.keys():
        new_input[feature] = new_input[feature].apply(
            lambda x: x.split(", ") if isinstance(x, str) else []
        )
        transformed = mlb_dict[feature].transform(new_input[feature])
        transformed_df = pd.DataFrame(
            transformed,
            columns=[f"{feature}_{label}" for label in mlb_dict[feature].classes_],
        )
        new_input = pd.concat(
            [new_input.drop(columns=[feature]), transformed_df], axis=1
        )
    new_input["Episodes"] = scaler_episodes.transform(new_input[["Episodes"]])
    new_input["Year"] = scaler_year.transform(new_input[["Year"]])
    return new_input


def get_prediction(pred_input):
    with open("models/random_forest_model.pkl", "rb") as file:
        model = pickle.load(file)
    pred = model.predict(get_formatted_input(pred_input))
    return "Popular" if pred[0] == 1 else "Unpopular"


popular_input = pd.DataFrame(
    {
        "Source": ["Original"],
        "Episodes": [28],
        "Rating": ["PG-13 - Teens 13 or older"],
        "Season": ["summer"],
        "Year": [2023],
        "Broadcast_Day": ["Mondays"],
        "Producers": ["Pierrot, TV Tokyo"],
        "Licensors": ["Crunchyroll"],
        "Studios": ["Madhouse"],
        "Genres": ["Action, Adventure"],
        "Themes": ["Vampire, Military"],
    }
)
unpopular_input = pd.DataFrame(
    {
        "Source": ["Original"],
        "Episodes": [0],
        "Rating": ["PG-13 - Teens 13 or older"],
        "Season": ["summer"],
        "Year": [2023],
        "Broadcast_Day": ["Mondays"],
        "Producers": ["Pierrot, TV Tokyo"],
        "Licensors": ["ADV Films"],
        "Studios": ["feel., Assez Finaud Fabric"],
        "Genres": ["Slice of Life"],
        "Themes": ["Vampire, Military"],
    }
)


print("Prediction1: ", get_prediction(popular_input))
print("Prediction2: ", get_prediction(unpopular_input))
