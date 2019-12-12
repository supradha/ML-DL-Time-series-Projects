Web traffic time-series data from Kaggle Competition

The training dataset consists of approximately 145k time series. Each of these time series represent a number of daily views of a different Wikipedia article, starting from July, 1st, 2015 up until December 31st, 2016. Each time series is provided the name of the article as well as the type of traffic that this time series represent (all, mobile, desktop, spider)


train_*.csv - contains traffic data. This a csv file where each row corresponds to a particular article and each column correspond to a particular date. Some entries are missing data. The page names contain the Wikipedia project (e.g. en.wikipedia.org), type of access (e.g. desktop) and type of agent (e.g. spider). In other words, each article name has the following format: 'name_project_access_agent' (e.g. 'AKB48_zh.wikipedia.org_all-access_spider').

key_*.csv - gives the mapping between the page names and the shortened Id column used for prediction

sample_submission_*.csv - a submission file showing the correct format

It is a discrete time series data. Hence we Indetify the stationarity of data. 
We identify the trend and seasonal parameters and evaluae with different models.