# Yelp Data Exploration

This project involves the data visualization and sentiment analysis of restaurants and eateries included in the [Yelp Open Dataset](https://www.yelp.com/dataset). In the first stage of the project I converted the 8.4 GB JSON formatted dataset into a SQLite database for efficient querying of the large dataset. I used CSV outputs of the SQL queries in the visualization and sentiment analysis portions of the project.

I performed interactive data visualization and exploration of the dataset using [bokeh](bokeh.pydata.org). The visualization revealed seasonal review rating trends, and a slowdown in the growth of user engagement over the past few years.

Finally, I performed sentiment analysis of 35,000 random user reviews of eateries in the dataset using NLP techniques such as lemmatization, TF-IDF, and word2vec. TF-IDF vectorization with tri-grams performed better than word2vec with training on 80% of the dataset. Logistic regression models had a higher accuracy and sensitivity, while gradient boosting models had a higher specificity than logistic regression. 

## Notebook
* [Data Visualization](https://nbviewer.jupyter.org/github/tcwou/Yelp-Data-Exploration/blob/master/CSV/Data%20Visualization.ipynb)
* [Sentiment Analysis](https://nbviewer.jupyter.org/github/tcwou/Yelp-Data-Exploration/blob/master/CSV/Sentiment%20Analysis.ipynb)
* [SQL Database and Queries](https://nbviewer.jupyter.org/github/tcwou/Yelp-Data-Exploration/blob/master/CSV/SQL%20Database%20and%20Queries.ipynb)

### Methods Used
* Machine Learning
* Data Visualization
* NLP
* Classification

### Technologies
* Python
* Pandas
* Scikit-learn
* Bokeh
