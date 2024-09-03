# EU-Data-Analysis
## Summary
The goal is to create a recommendation algorithm to recommend the best country in Europe for a specific profile.

Obviously this algortihms would be targeted at EU residents as the law make it easy and we don't have to take visas into account.
(Even tho some countries still have laws and quotas to limit inter EU migrations)

## Idea
### First personal ideas
My main two ideas are :
- find the people's criteria and which countries they live in to train an ai model that can predict the current profile best country
   * cons : no explaination as to why and not able to show statistics based on criterias, need a lot of data
- use the people's criteria to filter through the different data set available. Based on the different filter criteria intersect the coutries resulting and propose them to the user. (as it turns out to be the easiest algorithms to implement I will start with this one)

### External ideas
To help create new ideas I then asked llama genAI about ways of solving this problem :

#### Question asked
Depending on the profile of a person and multiple criterias. We have multiple datasets about the different european countries. What is the best way to find the more suitable country for the profile ?

#### Answer

A classic problem of multi-criteria decision analysis!

To find the most suitable country for a person's profile, you'll need to develop a systematic approach that considers multiple criteria and weights their importance. Here's a general framework to help you get started:

Define the profile and criteria: Identify the key characteristics of the person's profile (e.g., age, education, occupation, interests, language proficiency, etc.). Determine the relevant criteria to consider when evaluating countries. Some examples of criteria might include:
- Cost of living
- Job opportunities
- Language requirements
- Culture and lifestyle
- Education system
- Healthcare
- Safety and security
- Climate and geography
- Ease of integration

Gather and preprocess data: Collect datasets for each criterion, either from publicly available sources (e.g., World Bank, OECD, Eurostat) or through surveys/questionnaires. Ensure the data is clean, normalized, and in a suitable format for analysis.

Weight the criteria: Assign weights to each criterion based on their relative importance for the person's profile.
You can use techniques like:
- Expert judgment: Ask experts or the person themselves to assign weights.
- Survey analysis: Analyze survey responses to determine the importance of each criterion.
- Statistical methods: Use techniques like Principal Component Analysis (PCA) or factor analysis to identify the underlying structure of the criteria and assign weights.
- Calculate country scores: For each country, calculate a score for each criterion using the preprocessed data.
  You can use various methods, such as:
  - Simple additive weighting (SAW): Assign a score for each criterion and sum them up.
  - Weighted sum model (WSM): Multiply each criterion score by its weight and sum them up.
  - Multi-attribute decision analysis (MADA): Use techniques like TOPSIS, VIKOR, or ELECTRE to evaluate countries based on multiple criteria.
- Rank countries: Calculate an overall score for each country by aggregating the criterion scores. Rank the countries based on their overall scores to determine the most suitable country for the person's profile.
- Sensitivity analysis: Perform sensitivity analysis to test the robustness of the results by varying the weights, criteria, or data. This helps identify the most critical factors influencing the country ranking.
- Visualize and interpret results: Use visualization tools (e.g., bar charts, radar plots, heatmaps) to illustrate the country rankings and criterion scores. Interpret the results in the context of the person's profile and criteria.
Some popular algorithms and techniques for multi-criteria decision analysis include:

- TOPSIS (Technique for Order Preference by Similarity to Ideal Solution)
- VIKOR (VlseKriterijumska Optimizacija I Kompromisno Resenje)
- ELECTRE (Elimination and Choice Translating Reality)
- PROMETHEE (Preference Ranking Organization Method for Enrichment Evaluation)
- AHP (Analytic Hierarchy Process)

Choose the approach that best fits your specific problem and data. You may also consider using machine learning techniques, such as decision trees or clustering algorithms, to identify patterns in the data and support the decision-making process.

Remember to consider the limitations and uncertainties associated with the data and the decision-making process. The goal is to provide a well-informed recommendation, rather than a definitive answer.

### Temporary choice

It seems like after considering the different responses I decided to have a try with the TOPSIS technique first on a limited amount of criterias.

Analysis of EU data coming from Eurostat website : https://ec.europa.eu/eurostat/databrowser/explore/all/all_themes?lang=en&display=list&sort=category

List of useful websites :
 - https://data.gov/
 - https://statelibrary.ncdcr.libguides.com/c.php?g=635042&p=4441625

List of recommender systems :
