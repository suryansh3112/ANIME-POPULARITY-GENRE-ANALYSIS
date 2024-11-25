#### SER594: Experimentation

#### Analyzing Anime Popularity and Genre Trends

#### Suryansh Bhupesh Purohit

#### 24th November 2024

## Explainable Records

### Record 1

**Raw Data:** Id Name English_Name Type Source Episodes Airing Aired_From Aired_To Duration Rating Score Scored_By Rank Popularity Members Favorites Season Year Broadcast_Day Broadcast_Time Producers Licensors Studios Genres Themes
5114 Fullmetal Alchemist: Brotherhood Fullmetal Alchemist: Brotherhood TV Manga 64 FALSE 2009-04-05 00:00:00+00:00 2010-07-04 00:00:00+00:00 24 R - 17+ (violence & profanity) 9.09 2163268 2.0 3 3426057 228856 spring 2009 Sundays 17:00 ['Aniplex', 'Square Enix', 'Mainichi Broadcasting System', 'Studio Moriken'] ['Funimation', 'Aniplex of America'] ['Bones'] ['Action', 'Adventure', 'Drama', 'Fantasy'] ['Military']

Prediction Explanation:
Prediction: Popular
Explanation: The model classifies Fullmetal Alchemist: Brotherhood as popular due to its high-quality source material (Manga), a substantial number of episodes (64), favorable R rating, and release during a prime Spring season in 2009. The involvement of reputable studios like Bones and major licensors such as Aniplex further contribute to its widespread appeal.

### Record 2

**Raw Data:** Id Name English_Name Type Source Episodes Airing Aired_From Aired_To Duration Rating Score Scored_By Rank Popularity Members Favorites Season Year Broadcast_Day Broadcast_Time Producers Licensors Studios Genres Themes
37823 Conception Conception TV Game 12 FALSE 2018-10-10 00:00:00+00:00 2018-12-26 00:00:00+00:00 23 PG-13 - Teens 13 or older 4.58 52737 13370.0 1792 129987 170 fall 2018 Wednesdays 01:30 ['Sotsu'] ['Funimation'] ['Gonzo'] ['Action', 'Comedy', 'Fantasy', 'Romance'] ['Harem', 'Isekai', 'Parody']

Prediction Explanation:
Prediction: Unpopular
Explanation: Conception is unpopular because of the limited episode count (12), a Game as its source, and PG-13 rating, meaning smaller depth of content. Its release in the Fall season of 2018 with less recognized licensors and also niche themes such as Harem and Parody indicates poor audience engagement and appeal.

## Interesting Features

### Feature A

**Feature:** Source

**Justification:** The origin of any anime-Manga, Light Novel, or Game-often determines the depth in storytelling and what audiences would come to expect. For example, anime that originates from popular manga usually has a strong following and more developed storylines, which increases their popularity. However, anime that stems from games may attract audiences from a very specific niche, which can have an impact on their wider popularity.

### Feature B

**Feature:** Studios

**Justification:** The quality of the anime and its reception depend a lot on the studio producing it. Famous studios like Bones or Madhouse are well known for their great animation, storytelling, and flow, and often captivate viewership and popularity. Less popular or low-tier studios may make anime that sometimes has inconsistent quality; therefore, the audience is less interested in viewing.

## Experiments

### Varying A

**Prediction Trend Seen:** When varying the `Source` feature while keeping other features constant, the prediction trend shows that "Manga" and "Visual novel" sources tend to be classified as "Popular," while "Original", "Game", "Mixed media", and "Other" sources are classified as "Unpopular". This indicates that the model thinks certain source types like manga and visual novels for instance, are more popular because they have established fanbases or are well-recognized in the anime industry.

### Varying B

**Prediction Trend Seen:** When varying the feature `Studios`, keeping other features constant, the model's predictions are mostly dominated by the "Bones" studio, which gets classified as "Popular" quite frequently. On the other hand, studios like "Madhouse", "Pierrot Films", "DRAWIZ", "Kigumi", and "RAMS" get classified as "Unpopular" quite frequently. This may be an indication that the model has learned a bias toward certain studios that are historically more successful or well-known for producing popular anime.

### Varying A and B together

**Prediction Trend Seen:** In cases where `Source` and `Studios` vary together, the predictions indicate that certain combinations, such as "Manga" with "Bones," are always predicted to be "Popular". Conversely, certain combinations, such as "Original" with "DRAWIZ," get classified as "Unpopular". It seems that the joint effect of `Source` and `Studios` makes the predictions more detailed, with both features playing an important part in determining the output. That also shows that having one popular source, such as manga, increases the chances of a positive prediction even when allied with less popular studios.

### Varying A and B inversely

**Prediction Trend Seen:** Inverse variation in `Source` and `Studios`-for example, "Manga" with "RAMS" or "Original" with "Bones"-the trend indicates that there is a definite shift noted in the predictions. Specific combinations, such as "Manga" combined with "RAMS", still yield a prediction of "Popular", while "Original" combined with "Bones" tends to be "Popular" as well. This suggests that even though the model takes both features into consideration independently of each other, some combinations-even when one feature is considered less favorable-do not drastically alter the final prediction and this would suggest areas of flexibility or tolerance within the model.
