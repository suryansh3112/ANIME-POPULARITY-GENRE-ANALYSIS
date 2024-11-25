import pandas as pd
import re


def convert_to_minutes(duration):
    if pd.isna(duration):
        return None
    total_minutes = 0
    total_seconds = 0
    hr_match = re.search(r"(\d+)\s*hr", duration)
    min_match = re.search(r"(\d+)\s*min", duration)
    sec_match = re.search(r"(\d+)\s*sec", duration)

    if hr_match:
        total_minutes += int(hr_match.group(1)) * 60
    if min_match:
        total_minutes += int(min_match.group(1))
    if sec_match:
        total_seconds += int(sec_match.group(1))

    total_minutes += total_seconds // 60

    return total_minutes


def get_season(month):
    if month in [12, 1, 2]:
        return "winter"
    elif month in [3, 4, 5]:
        return "spring"
    elif month in [6, 7, 8]:
        return "summer"
    else:
        return "fall"


def process_data():
    output_filename = "data_processed/anime_processed_data.csv"

    df = pd.read_csv("data_orignal/anime_dataset.csv")

    # only keep tv, movie, ova, ona types from db
    df = df[df["Type"].isin(["TV", "Movie", "OVA", "ONA"])]

    # removing entries that don't have score
    df = df.dropna(subset=["Score"])

    # converting into datestring from string
    df["Aired_From"] = pd.to_datetime(df["Aired_From"], errors="coerce")
    df["Aired_To"] = pd.to_datetime(df["Aired_To"], errors="coerce")

    # Filling missing episodes
    current_date = pd.Timestamp("2024-11-24", tz="UTC")
    df["estimated_episodes"] = ((current_date - df["Aired_From"]).dt.days // 7).astype(
        float
    )
    df["Episodes"] = df["Episodes"].fillna(df["estimated_episodes"])
    # removing entries without episode
    df = df.dropna(subset=["Episodes", "Aired_From"])
    df["Episodes"] = df["Episodes"].astype(int)
    df = df.drop(columns=["estimated_episodes"])

    # converting duration from string to minutes
    df["Duration"] = df["Duration"].apply(convert_to_minutes)

    # Filling missing English_Name
    df["English_Name"] = df["English_Name"].fillna(df["Name"])

    # removing unnecessary columns
    df = df.drop(columns=["Japanese_Name", "Url", "Status"])

    # Filling Season and year column

    df["Year"] = df["Year"].fillna(df["Aired_From"].dt.year)
    df["Season"] = df["Season"].fillna(df["Aired_From"].dt.month.apply(get_season))

    # Renaming Scored by column
    df.rename(columns={"Scored By": "Scored_By"}, inplace=True)

    # Converting column to int
    df["Scored_By"] = df["Scored_By"].astype(int)
    df["Year"] = df["Year"].astype(int)

    single_label_categorical = ["Source", "Rating", "Season", "Broadcast_Day"]
    for feature in single_label_categorical:
        df[feature] = df[feature].fillna("Unknown")

    multi_label_categorical = ["Producers", "Licensors", "Studios", "Genres", "Themes"]

    for feature in multi_label_categorical:
        df[feature] = df[feature].apply(
            lambda x: x.split(", ") if isinstance(x, str) else []
        )

    # Converting processed data to csv
    df.to_csv(output_filename, index=False)
