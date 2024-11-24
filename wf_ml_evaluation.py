import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, MultiLabelBinarizer

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
data["Popularity_Output"] = data["Score"].apply(lambda x: 1 if x > score_median else 0)
data = data.drop(columns=["Score"])

scaler = MinMaxScaler()
data["Episodes"] = scaler.fit_transform(data[["Episodes"]])
data["Year"] = scaler.fit_transform(data[["Year"]])

for feature in single_label_categorical:
    data[feature] = pd.factorize(data[feature])[0]

for feature in multi_label_categorical:
    mlb = MultiLabelBinarizer()
    transformed_data = mlb.fit_transform(data[feature])
    transformed_df = pd.DataFrame(
        transformed_data, columns=[f"{feature}_{label}" for label in mlb.classes_]
    )
    data = pd.concat([data.drop(columns=[feature]), transformed_df], axis=1)

data = data.drop(columns=["Type"])

X = data.drop(columns=["Popularity_Output"])
y = data["Popularity_Output"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=40, stratify=y
)
print(X_test)
print(y_test)

print("Training data shape:", X_train.shape)
print("Test data shape:", X_test.shape)
print("yTraining data shape:", y_train.shape)
print("yTest data shape:", y_test.shape)
print("y_train distribution:\n", y_train.value_counts(normalize=True))
print("y_test distribution:\n", y_test.value_counts(normalize=True))
