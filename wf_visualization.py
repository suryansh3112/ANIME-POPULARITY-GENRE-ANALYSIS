import pandas as pd
from enum import Enum
import matplotlib.pyplot as plt
import os
import matplotlib.ticker as mtick


class AnimeType(Enum):
    TV = 1
    Movie = 2
    ONA = 3
    OVA = 4


def get_result_structure():
    return {"quantitative": [], "qualitative": []}


def get_quantitative_summary(df, feature):
    min_val = df[feature].min()
    median_val = df[feature].median()
    max_val = df[feature].max()
    return (feature, min_val, median_val, max_val)


def get_qualitative_summary(df, feature):
    num_categories = df[feature].nunique()
    most_freq_category = df[feature].value_counts().idxmax()
    least_freq_category = df[feature].value_counts().idxmin()
    return (feature, num_categories, most_freq_category, least_freq_category)


def write_feature(file, summary, summary_names):
    file.write(f"\t{summary[0]}:\n")
    file.write(f"\t\t{summary_names[0]}: {summary[1]}\n")
    file.write(f"\t\t{summary_names[1]}: {summary[2]}\n")
    file.write(f"\t\t{summary_names[2]}: {summary[3]}\n")


def generate_summary_text_file(results):
    output_file = "data_processed/summary.txt"
    with open(output_file, "w") as file:
        for anime_type, summaries in results.items():
            file.write(f"Type: {anime_type}\n")
            file.write(f"Quantitative Features:\n")
            for summary in summaries["quantitative"]:
                write_feature(file, summary, ["Min", "Median", "Max"])

            file.write(f"Qualitative Features:\n")
            for summary in summaries["qualitative"]:
                write_feature(
                    file,
                    summary,
                    [
                        "Number of Categories",
                        "Most Frequent Category",
                        "Least Frequent Category",
                    ],
                )
            file.write("\n")


def generate_correlations_text_file(corr):
    output_file = "data_processed/correlations.txt"
    with open(output_file, "w") as file:
        for name, correlation_matrix in corr:
            file.write(f"Correlations for Type - {name}:\n")
            file.write(f"{correlation_matrix}\n")
            file.write("\n")


def plot_quantitative_features(anime_types, quantitative_features):

    for curr_df, name in anime_types:
        os.makedirs(f"visuals/{name}", exist_ok=True)
        for i in range(len(quantitative_features)):
            for j in range(i + 1, len(quantitative_features)):
                plt.figure(figsize=(10, 6))
                plt.scatter(
                    curr_df[quantitative_features[i]],
                    curr_df[quantitative_features[j]],
                    alpha=0.5,
                    s=5,
                )
                max_x = curr_df[quantitative_features[i]].max()
                max_y = curr_df[quantitative_features[j]].max()
                if max_y > 1_000_000:
                    plt.gca().yaxis.set_major_formatter(
                        mtick.FuncFormatter(lambda x, _: f"{x * 1e-6:.1f}M")
                    )
                if max_x > 1_000_000:
                    plt.gca().xaxis.set_major_formatter(
                        mtick.FuncFormatter(lambda x, _: f"{x * 1e-6:.1f}M")
                    )
                plt.title(
                    f"Scatter Plot: {quantitative_features[i]} vs {quantitative_features[j]} ({name})"
                )
                plt.xlabel(quantitative_features[i])
                plt.ylabel(quantitative_features[j])
                plt.grid(True, which="both", linestyle="--", linewidth=0.5)
                plt.savefig(
                    f"visuals/{name}/scatter_{quantitative_features[i]}_{quantitative_features[j]}.png"
                )
                plt.close()


def plot_qualitative_features(anime_types, qualitative_features):
    for curr_df, name in anime_types:
        os.makedirs(f"visuals/{name}", exist_ok=True)
        for feature in qualitative_features:
            curr_df[feature].value_counts().plot(kind="bar")
            plt.title(f"Histogram of {feature} ({name})")
            plt.xlabel(feature)
            plt.ylabel("Frequency")
            plt.grid(axis="y", linestyle="--", alpha=0.6)
            plt.xticks(rotation=45, ha="right")
            plt.tight_layout()
            plt.savefig(f"visuals/{name}/histogram_{feature}.png")
            plt.close()


def visualize_data():
    df = pd.read_csv("data_processed/anime_processed_data.csv")
    tv_df = df[df["Type"] == AnimeType.TV.name]
    movie_df = df[df["Type"] == AnimeType.Movie.name]
    ona_df = df[df["Type"] == AnimeType.ONA.name]
    ova_df = df[df["Type"] == AnimeType.OVA.name]

    anime_types = [
        (tv_df, AnimeType.TV.name),
        (movie_df, AnimeType.Movie.name),
        (ona_df, AnimeType.ONA.name),
        (ova_df, AnimeType.OVA.name),
    ]
    quantitative_features = ["Score", "Scored_By", "Members"]
    qualitative_features = ["Rating", "Source"]

    results = {
        AnimeType.TV.name: get_result_structure(),
        AnimeType.Movie.name: get_result_structure(),
        AnimeType.ONA.name: get_result_structure(),
        AnimeType.OVA.name: get_result_structure(),
    }

    for curr_df, name in anime_types:
        for feature in quantitative_features:
            summary = get_quantitative_summary(curr_df, feature)
            results[name]["quantitative"].append(summary)

        for feature in qualitative_features:
            summary = get_qualitative_summary(curr_df, feature)
            results[name]["qualitative"].append(summary)

    generate_summary_text_file(results)

    corr = []
    for curr_df, name in anime_types:
        corr.append((name, curr_df[quantitative_features].corr().round(3)))
    generate_correlations_text_file(corr)

    plot_quantitative_features(anime_types, quantitative_features)
    plot_qualitative_features(anime_types, qualitative_features)
