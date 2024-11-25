#### SER594: Machine Learning Evaluation

#### Analyzing Anime Popularity and Genre Trends

#### Suryansh Bhupesh Purohit

#### 24th November 2024

## Evaluation Metrics

### Metric 1

**Name:** Accuracy

**Choice Justification:** Accuracy measures the proportion of correct predictions out of total. For this problem, where the target is binary (Popularity_Output), accuracy gives a general overview of the model's performance. It is particularly useful when class distributions are relatively balanced, as in this dataset (stratified sampling ensured balance).

**Interpretation:** Accuracy is defined as the percentage of the total number of predictions that the model predicted correctly. The higher the accuracy, the better the model.

### Metric 2

**Name:** F1-Score

**Choice Justification:** The F1-score takes into account both precision and recall by calculating their harmonic mean. This is particularly relevant in this problem of classification, as we want to avoid biases toward one class in order to balance false positives and false negatives.

**Interpretation:** The F1-score ranges from 0 to 1, with higher values indicating better balance between precision and recall.

## Alternative Models

### Alternative 1: Random Forest (100 estimators)

**Construction:**
Model: RandomForestClassifier from sklearn
Parameters: n_estimators=100, criterion="entropy", random_state=17

**Evaluation:**

1. **Accuracy:** 81.33%
2. **F1-Score:** 0.8671<br>

This model did best on both accuracy and F1-score, which means that it was up to the task of modeling the complexity of the dataset.

### Alternative 2: Random Forest (200 estimators)

**Construction:**
Model: RandomForestClassifier from sklearn
Parameters: n_estimators=200, criterion="gini", random_state=17

**Evaluation:**

1. **Accuracy:** 80.82%
2. **F1-Score:** 0.8640<br>

Further increases in the number of estimators did not increase accuracy or F1-score from the 100-estimator Random Forest. It likely added unnecessary complexity without much gain.

### Alternative 3: Gradient Boosting Classifier

**Construction:**
Model: GradientBoostingClassifier from sklearn
Parameters: Default with random_state=17

**Evaluation:**

1. **Accuracy:** 78.06%
2. **F1-Score:** 0.8448<br>

This model showed reasonable performance but was far from the Random Forest classifiers. Gradient Boosting might require further parameter tuning for better results.

### Alternative 4: Logistic Regression

**Construction:**
Model: LogisticRegression from sklearn
Parameters: max_iter=1000, random_state=17

**Evaluation:**

1. **Accuracy:** 78.27%
2. **F1-Score:** 0.8409<br>

Logistic Regression had scores similar to Gradient Boosting Classifier. It is a linear model, and thus it is likely less suited to the non-linear relationships in the dataset.

## Best Model

**Model:** Random Forest (100 estimators)

**Justification:**
The best performance metrics were obtained with a Random Forest model using 100 estimators and criterion="entropy":

**Accuracy:** 81.33%<br>

**F1-Score:** 0.8671<br>

This model's balance of interpretability, computational efficiency, and effectiveness makes it an ideal choice for this problem.
