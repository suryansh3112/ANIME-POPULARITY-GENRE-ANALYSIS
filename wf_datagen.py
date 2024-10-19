import csv
import re
import requests
import json
import time

BATCH_SIZE = 40


def getAnimePageData(page):
    url = f"https://api.jikan.moe/v4/top/anime?page={page}"
    data = requests.get(url)

    attempts = 0
    while attempts < 2 and data.status_code != 200:
        time.sleep(1)
        attempts += 1
        page = requests.get(url)
    if attempts > 0:
        print(f"Required attempts {attempts} for page {page}")
    return data


def getFormattedAnimeData(data):
    anime = {}
    anime["Id"] = data.get("mal_id")

    anime["Name"] = data.get("title")

    anime["English_Name"] = data.get("title_english")

    anime["Japanese_Name"] = data.get("title_japanese")

    anime["Url"] = data.get("url")

    anime["Type"] = data.get("type")

    anime["Source"] = data.get("source")

    anime["Episodes"] = data.get("episodes")

    anime["Status"] = data.get("status")

    anime["Airing"] = data.get("airing")

    anime["Aired_From"] = data.get("aired", {}).get("from")

    anime["Aired_To"] = data.get("aired", {}).get("to")

    anime["Duration"] = data.get("duration")

    anime["Rating"] = data.get("rating")

    anime["Score"] = data.get("score")

    anime["Scored By"] = data.get("scored_by")

    anime["Rank"] = data.get("rank")

    anime["Popularity"] = data.get("popularity")

    anime["Members"] = data.get("members")

    anime["Favorites"] = data.get("favorites")

    anime["Season"] = data.get("season")

    anime["Year"] = data.get("year")

    anime["Broadcast_Day"] = data.get("broadcast", {}).get("day")

    anime["Broadcast_Time"] = data.get("broadcast", {}).get("time")

    anime["Producers"] = ", ".join(
        [producer["name"] for producer in data.get("producers", [])]
    )

    anime["Licensors"] = ", ".join(
        [license["name"] for license in data.get("licensors", [])]
    )

    anime["Studios"] = ", ".join([studio["name"] for studio in data.get("studios", [])])

    anime["Genres"] = ", ".join([genre["name"] for genre in data.get("genres", [])])

    anime["Themes"] = ", ".join([theme["name"] for theme in data.get("themes", [])])

    return anime


def save_as_csv(anime_list, csv_filename, pageNo):
    mode = "a" if pageNo > BATCH_SIZE else "w"
    with open(csv_filename, mode, newline="", encoding="utf-8") as file:
        fieldnames = anime_list[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        if pageNo == BATCH_SIZE:
            writer.writeheader()
        writer.writerows(anime_list)
        print(f"Saved data for till page {pageNo}")
        anime_list.clear()


def fetch_and_save_anime_data():
    anime_list = []
    csv_filename = "data_orignal/anime_dataset.csv"
    count = 0
    pageNo = 1

    while True:
        data = getAnimePageData(pageNo)
        if data.status_code != 200:
            print(f"Failed to retrieve data for page {pageNo} due to API error.")
            break

        jsonData = data.json()
        if "data" in jsonData:
            for anime in jsonData["data"]:
                anime_data = getFormattedAnimeData(anime)
                anime_list.append(anime_data)
                count += 1
            time.sleep(1)
            if pageNo % BATCH_SIZE == 0:
                save_as_csv(anime_list, csv_filename, pageNo)

        else:
            print(f"Data key not present for page Number: {pageNo}")
            break
        if jsonData.get("pagination", {}).get("has_next_page"):
            pageNo += 1
        else:
            break
    if anime_list:
        save_as_csv(anime_list, csv_filename, pageNo)

    print(f"Saved {count} animes in csv")
