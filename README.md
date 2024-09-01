# EU-Data-Analysis
The goal is to create a recommendation algorithm to recommend the best country in Europe for a specific profile.

Obviously this algortihms would be targeted at EU residents as the law make it easy and we don't have to take visas into account.
(Even tho some countries still have laws and quotas to limit inter EU migrations)

My main two ideas are :
- find the people's criteria and which countries they live in to train an ai model that can predict the current profile best country
   * cons : no explaination as to why and not able to show statistics based on criterias, need a lot of data
- use the people's criteria to filter through the different data set available. Based on the different filter criteria intersect the coutries resulting and propose them to the user. (as it turns out to be the easiest algorithms to implement I will start with this one)

Analysis of EU data coming from Eurostat website : https://ec.europa.eu/eurostat/databrowser/explore/all/all_themes?lang=en&display=list&sort=category

List of useful websites :
 - https://data.gov/
 - https://statelibrary.ncdcr.libguides.com/c.php?g=635042&p=4441625

List of recommender systems :
