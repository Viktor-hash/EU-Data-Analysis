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

I m going with my own ranking function as the other method are not specific and simple enough.

The function will look like something like this for two criterias of one alternative (e.g earnings and tax):

w(x) = weight of x
w(y) = weight of y
x = earnings criteria
y = tax criteria 

for every criteria (I am taking x as an example here):
- if preference is LOW then we do x = 1/x
- if preference is MID then we do x = 1/abs(x - mean(allAlternativeOfx))

f(x,y) = w(x) * x + w(y) * y

Doing this for every alternatives will give a ranking that can be sorted by descending order.

## Application

#### Perference/Weights

The weight will be evaluated by the following values :
- HIGH
- MID
- LOW
- NEUTRAL

The preference will be evaluated by the following values :
- HIGH
- MID
- LOW

The following preferences/weights will be asked : 

I. Economic Factors

Cost of living: Can the person afford the living expenses, including housing, food, transportation, and healthcare?
Job opportunities: Are there job opportunities in the person's field, and what are the salary ranges?
Taxes: What are the tax implications for the person, including income tax, sales tax, and other taxes?

II. Safety and Security

Crime rate: Is the country considered safe, with low crime rates?
Terrorism and conflict: Is the country prone to terrorism or conflict?
Natural disasters: Is the country vulnerable to natural disasters, such as earthquakes, hurricanes, or floods?

III. Culture and Lifestyle

Language: Is the official language spoken by the person, or are there opportunities to learn the language?
Cultural norms: Are the cultural norms and values aligned with the person's own values and lifestyle?
Social life: Are there opportunities to socialize and connect with like-minded people?

IV. Education and Healthcare

Education system: Is the education system of high quality, with access to good schools and universities?
Healthcare system: Is the healthcare system of high quality, with access to good medical facilities and services?
Access to specialized care: Are there specialized medical services available, such as mental health services or specialized medical treatments?

V. Environment and Climate

Climate: Is the climate suitable for the person, with comfortable temperatures and minimal extreme weather conditions?
Environmental quality: Is the air and water quality good, with minimal pollution?
Access to nature: Are there opportunities to connect with nature, such as parks, beaches, or mountains?

VI. Visa and Immigration Requirements

Visa requirements: Are the visa requirements straightforward, with minimal bureaucratic hurdles?
Immigration process: Is the immigration process efficient, with clear guidelines and timelines?
Citizenship opportunities: Are there opportunities to obtain citizenship, with clear requirements and benefits?

VII. Infrastructure and Transportation

Transportation options: Are there reliable and efficient transportation options, such as public transportation, airports, or roads?
Internet and communication: Is the internet and communication infrastructure reliable and fast?
Access to amenities: Are there amenities such as shopping centers, restaurants, and entertainment options available?

VIII. Personal Freedoms

Freedom of speech: Is there freedom of speech, with minimal censorship or restrictions?
LGBTQ+ rights: Are LGBTQ+ rights protected, with minimal discrimination or persecution?
Women's rights: Are women's rights protected, with minimal discrimination or inequality?

Reference : https://web.archive.org/web/20180603090537id_/http://www.ijrter.com/papers/volume-3/issue-3/study-approach-technique-for-order-of-preference-by-similarity-to-ideal-solution-topsis.pdf

Analysis of EU data coming from Eurostat website : https://ec.europa.eu/eurostat/databrowser/explore/all/all_themes?lang=en&display=list&sort=category

List of useful websites :
 - https://data.gov/
 - https://statelibrary.ncdcr.libguides.com/c.php?g=635042&p=4441625

List of recommender systems :
