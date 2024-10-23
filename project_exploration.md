#### SER594: Exploratory Data Munging and Visualization

#### Exploring and Visualizing Anime Data

#### Suryansh Bhupesh Purohit

#### 21 October 2024

## Basic Questions

**Dataset Author(s):** This data was sourced from Jikan API, which is unofficial api for MyAnimeList.

**Dataset Construction Date:** 18 October 2024

**Dataset Record Count:** 27666

**Dataset Field Meanings:**

1.  Id: MyAnimeList ID of the anime
2.  Name: Title of anime
3.  English_Name: Official English title of anime
4.  Japanese_Name: Japanese title of anime
5.  Url: url to anime page on MyAnimeList
6.  Type: Format of Anime
7.  Source: Official Source of anime
8.  Episodes: Total number of Episodes
9.  Status: Current airing status
10. Airing: Boolean for airing
11. Aired_From: Date when anime started airing
12. Aired_To: Date when anime finished airing
13. Duration: Duration of anime
14. Rating: Content Rating for anome
15. Score: Average user rating for anime
16. Scored By: Number of users who have submitted rating for anime
17. Rank: Rank of anime based on score
18. Popularity: The rank of the anime based on how many users have added it to their lists (watching, completed, plan to watch, etc.)
19. Members: The total number of MyAnimeList users who have added the anime to their lists (e.g., watching, completed).
20. Favorites: The number of users who have marked the anime as one of their favorites.
21. Season: The season anime aired in.
22. Year: The year anime started airing.
23. Broadcast_Day: The day of week anime was broadcast.
24. Broadcast_Time: The time of day anime was broadcast.
25. Producers: The companies responsible for the overall production of the anime
26. Licensors:The companies that hold the legal rights to distribute the anime
27. Studios: The animation studios responsible for the production of the anime.
28. Genres:The genres that describe the anime
29. Themes: The themes present in the anime

**Dataset File Hash(es):** Anime dataset used was generated through Jikan Api, so there is no file to hash. Data was gathered by calling api: `https://api.jikan.moe/v4/top/anime?page={page}`. The data was collected page by page (wf_datagen.py). It took a total of 55 minutes.

## Interpretable Records

### Record 1

**Raw Data:**
Id Name English_Name Japanese_Name Url Type Source Episodes Status Airing Aired_From Aired_To Duration Rating Score Scored By Rank Popularity Members Favorites Season Year Broadcast_Day Broadcast_Time Producers Licensors Studios Genres Themes
52991 Sousou no Frieren Frieren: Beyond Journey's End 葬送のフリーレン https://myanimelist.net/anime/52991/Sousou_no_Frieren TV Manga 28 Finished Airing FALSE 2023-09-29T00:00:00+00:00 2024-03-22T00:00:00+00:00 24 min per ep PG-13 - Teens 13 or older 9.33 521212 1 194 918309 54321 fall 2023 Fridays 23:00 Aniplex, Dentsu, Shogakukan-Shueisha Productions, Nippon Television Network, TOHO animation, Shogakukan Crunchyroll Madhouse Adventure, Drama, Fantasy

**Interpretation:** This record is of anime Sousou no Frieren with id being 52991. It english and japanese name are provided. The url is provided. The format of this anime is TV, sourced from manga and it has 28 episodes. It has finished airing. It started on 29th september 2023 and ended on22nd March 2024. It had 24 min episodes. It rating was PG-13 - Teens 13 or older. It has a score of 9.33 scored by 521212 users. It's rank is 1 and popularity rank 194. It has 918309 members and is favorited by 54321 users. It started airing in fall 2023 on Fridays at 11pm. Anime's producers are Aniplex, Dentsu, Shogakukan-Shueisha Productions, Nippon Television Network, TOHO animation, Shogakukan. Crunchyroll is anime's licensor and Madhouse studio has created the anime. The genre of anime is Adventure, Drama, Fantasy. Theme field is missing.
This record is resonable with highest score in tv format, large audience and strong production backing

### Record 2

**Raw Data:** Id Name English_Name Japanese_Name Url Type Source Episodes Status Airing Aired_From Aired_To Duration Rating Score Scored By Rank Popularity Members Favorites Season Year Broadcast_Day Broadcast_Time Producers Licensors Studios Genres Themes
39486 Gintama: The Final Gintama: The Very Final 銀魂 THE FINAL https://myanimelist.net/anime/39486/Gintama__The_Final Movie Manga 1 Finished Airing FALSE 2021-01-08T00:00:00+00:00 1 hr 44 min PG-13 - Teens 13 or older 9.04 75673 7 1543 158158 4365 TV Tokyo, Aniplex, Dentsu, Bandai, Warner Bros. Japan, Shueisha Eleven Arts Bandai Namco Pictures Action, Comedy, Drama, Sci-Fi Gag Humor, Historical, Parody, Samurai

**Interpretation:** The name of anime is Gintama: The Final, and has english and japanese titles. The url is provided. The format for this anime is movie sourced from manga. It has one episode which is basically one movie. It has finished airing. It was released 8th January 2021. Duration of movie is 1hr 44 min with its rating being PG-13 - Teens 13 or older. It has a score of 9.04 scored by 75673 users. It's rank is 7 and popularity rank 1543. It has 158158 members and favorited by 4365 users. The season,year, broadcast day and time field are empty. It is produced by TV Tokyo, Aniplex, Dentsu, Bandai, Warner Bros. Japan, Shueisha, licensed by Eleven Arts created by Bandai Namco Pictures(Studio). It has Action, Comedy, Drama, Sci-Fi genre and theme are Gag Humor, Historical, Parody, Samurai.
This record is consistent with the real world data of Gintama: The Final, which is the final movie in the long-running Gintama series, known for its blend of action, comedy, and dramatic storytelling. Its high rating reflects the success of the movie as the concluding part of a beloved series.

## Background Domain Knowledge

Anime is a form of animation originating in Japan. It has become a global cultural phenomenon known for its distinct art style, complex storytelling, and diverse genres. Unlike other cartoons, it targets a broad audience, tackling themes that range from emotional and psychological to action packed adventures. Popular anime series like Attack on Titan and Fullmetal Alchemist: Brotherhood explore topics such as human nature, war, and power, making anime appealing to both young and adult viewers.

One key factor in anime's success is its connection to manga which is equivalent to comics. Many anime series, such as Naruto and Demon Slayer, are adapted from manga, ensuring a built-in audience and solidifying anime's role as a cross-media cultural force. This correlation between manga and anime has helped the growth of both industries with popular titles transitioning smoothly between the two.

Anime’s global rise has also been popularized by online streaming platforms like Crunchyroll and Netflix, making it more accessible to international audiences. Its global appeal has grown even stronger with fan communities that engage in cosplay, conventions, and fan-driven content, helping anime transcend cultural boundaries. Anime’s influence has even extended into non-Japanese media, with works like Avatar: The Last Airbender drawing inspiration from its style and storytelling.

In summary, anime’s combination of visual animations, engaging narratives, and cultural impact has established it as a dominant force in global entertainment.

1. **"The Anime Encyclopedia: A Guide to Japanese Animation Since 1917"**

- **Authors:** Jonathan Clements and Helen McCarthy
- **ISBN:** 978-1933330178

2. **"The Soul of Anime: Collaborative Creativity and Japan's Media Success Story"**

- **Authors:** Ian Condry
- **ISBN:** 978-0822353920

3. **"Japanese Visual Culture: Explorations in the World of Manga and Anime"**

- **Editor:** Mark W. MacWilliams
- **ISBN:** 978-0765610707

## Dataset Generality

This dataset is gathered from Jikan API is representative of the anime industry in terms of popularity, scoring, and viewership across various anime formats (TV, Movies, ONA, and OVA). The quantitative features such as Score, Scored By, and Members allows comprehensive understanding of audience preferences. The wide range of scores, from a minimum of 1.88 to a maximum of 9.33, and the large number of users who scored these anime indicate substantial variation, representing real-world viewer opinions. Qualitative features like Rating and Source further provide insight into content restrictions and the origin of stories, aligning well with how anime is consumed across different age groups and genres. The high correlations between Scored By and Members across all types demonstrate consistent audience engagement, making the dataset reflective of real-world distribution.

## Data Transformations

### Transformation 1: Filtering by Type

**Description:** This filters data based on type and keeps TV, Movie, OVA, and ONA.

**Soundness Justification:** This transformation does not change semantics of data because it focuses on relevent categories for analysis. By removing irrelevant types, we ensure that our analysis remains focused on the dataset's intended purpose without discarding usable data from the remaining categories.

### Transformation 2: Dropping Entries without Score

**Description:** Removed Entries which didn't have scores

**Soundness Justification:** Scores are critical for evaluating popularity of anime. By dropping these entries, we ensure that the dataset consists only of records with valid scores, thus maintaining the integrity of the analysis. This operation does not introduce errors or outliers as we are only removing non-informative data.

### Transformation 3: Date Conversion

**Description:** Converting string to date for Aired_From and Aired_To columns

**Soundness Justification:** This converts columns with date strings to datetime object, which helps in using this data. The parameter `errors="coerce"` manages any conversion errors, turning invalid dates into NaT without including errors or outliers.

### Transformation 4: Filling Missing Episodes

**Description:** The records with missing episodes are estimated by computing the difference between the current date and the "Aired_From" date, filled in the "Episodes" column.

**Soundness Justification:** This is a reasonable approximation of missing data without any added bias. The transformation assumes a weekly release schedule and does not reject useable data; thus, it maintains the integrity of the dataset as a whole.

### Transformation 5: Converting Duration

**Description:** Converting duration from string to minutes

**Soundness Justification:** This transformation unifies the unit to minutes from string that include hours, minutes and seconds. As we are just changing the format of the durations, there is no chance of introducing errors or outliers, which means that numerical analysis can be done.

### Transformation 6: Filling Missing English Names

**Description:** Missing entries in the column "English_Name" are filled from the "Name" column.

**Soundness Justification:** This transformation ensures that each entry will have an English name associated with it, making it more usable, but does so in a manner that has not affected the original semantics of the dataset.

### Transformation 7: Dropping Unnecessary Columns

**Description:**
The columns such as "Japanese_Name", "Url", and "Status" which are unnecessary for analysis are dropped from the dataset.

**Soundness Justification:**
This operation does not affect the semantics of the remaining data but rather simplifies the dataset for analysis. Removing extra information reduces complexity without discarding usable data or introducing errors.

### Transformation 8: Fill Missing Year and Season

**Description:**
The "Year" and "Season" columns are filled using values from the "Aired_From" date where they are missing.

**Soundness Justification:**
This maintains the same semantics since all the entries refer to a plausible year and season information. There is no injection of errors since information has been inferred from other data, as opposed to conjecturing arbitrary values.

### Transformation 9: Column Renaming

**Description:**
Rename the column "Scored By" to "Scored_By" for consistency.

**Soundness Justification:**
It does not impact the semantics of the data.

### Transformation 10: Type Conversion

**Description:**
Columns like "Scored_By", "Year" are casted into integer type.

**Soundness Justification:**
These columns need to be converted to their respective data types in order for the data to become analytically viable.

## Visualizations

### Visual 1: Histogram of Rating (TV)

**Analysis:** Most of the data falls into the category "PG-13 - Teens 13 or older", which dominates this distribution with the highest frequency. That might be a good implication that most of the TV shows are targeted for teen audiences and diminish considerably in number for other shows targeted either for children, or with higher, more adult content, such as "R+ - Mild Nudity" and "R - 17+ (violence & profanity)".

### Visual 2: Histogram of Source (TV)

**Analysis:** The most common source types for works of this type are "Manga," then "Original," and finally "Light novels." This indicates a trend that media formats like manga and light novels are highly utilized in making adaptations for TV, while other media formats such as "Picture book" or "Radio" hardly ever act as a source.

### Visual 3: Scatter Plot of Score vs. Scored_By (TV)

**Analysis:** It follows that the more the score increases, the more users rate shows in TV. There is even an evident spike around the 8 to 9 score range, where a large number of shows have much higher rating participations in terms of the number of users. That means, in other words, the higher-rated shows receive more scores from users. However, at the low-scoring end, most the shows achieve fewer ratings.

### Visual 4: Scatter Plot of Scored_By vs. Year (TV)

**Analysis:** From the plot, we can observe that recent TV shows (later than 2010) have more ratings compared to older shows. This may be due to growing popularity on online platforms and anime in general, since there is a clear increase in the number of ratings while moving from the 1990s to the 2020s.

### Visual 5: Scatter Plot of Score vs. Year (TV)

**Analysis:** From this graph, it is deducible that most of the TV series, ranging from the 1990s to the 2020s, fall within the score range of 6 to 8. While some outliers could result in higher or even lower scores, there is no apparent shifting of the trends of scores across time to really indicate that the general perception of the quality of the shows remains relatively similar across decades.
