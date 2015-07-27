     1) Introduction
 I am competing on a Kaggle competition called Give Me Some Credit. According to the website: 

‘Banks play a crucial role in market economies. They decide who can get finance and on what terms and can make or break investment decisions. For markets and society to function, individuals and companies need access to credit. 
Credit scoring algorithms, which make a guess at the probability of default, are the method banks use to determine whether or not a loan should be granted. This competition requires participants to improve on the state of the art in credit scoring, by predicting the probability that somebody will experience financial distress in the next two years.
The goal of this competition is to build a model that borrowers can use to help make the best financial decisions.’



2) Description of your data set and how it was obtained
The competition provided historical data for 250,000 borrowers. The data was broken into test and train data. Training data contains an additional feature: ‘Serious delinquency faced in the past two years’, the objective is to calculate the probability of the same for the borrowers in test data. 


3) Description of any pre-processing steps you took
Both data sets had multiple missing observations in the ‘Income’ and ‘Number of dependents’ features. The average and the dependent in both sets was close to zero, and the most frequent dependent was also zero. I used Scikit learn’s preprocessor to  impute the most frequent observation(Zero) to fill the values. 

I used KNNRegressor to impute missing values in the income field. I split the training data into two sets: those without missing income and those with missing income. I further split the data into test and train, and evaluated my KNNRegressor using Root Mean Squared error. I then used the KNNRegressor to impute missing income in the training data. I repeated the process for test data. 

Further cleaning idea: It looks like many observations in the income field are off by 100s(per discussion on the Kaggle forum); I need a way to clean it.

3) What you learned from exploring the data, including visualizations

4) How you chose which features to use in your analysis

First, I created an entirely new debt ratio column using imputed income.  I am working on creating new features, and this snippet from the eventual winners in the forum is bound to be of great help: 
	Given that we had only 10 features in the original set, it was necessary to use some ingenuity to come up with suitable new ones. To take your example - while Dependents * Age may not be a good feature, AvgDependentsIn10YearAgeBracket may be. You can use pretty much anything to produce new features - products, sums, ratios, removing outliers, transforming the data (e.g. converting to log values), computing distances (euclidean, levenshtein),  using ranking methods (e.g. assign rank based on total debt). The sky is the limit here - sometimes the craziest combinations work. You also need some way to determine which features have predictive power - see "summary" function in R.

Potential Features: 
	- Income >1
	- 
5)Details of your modeling process, including how you selected your models and validated them
So far, I’ve used logistical regression using features provided by the competition and ended with a relatively unimpressive AOC score(.797, the benchmark is .864249). I’d like to ruse the following models in the future: 
LR with additional features.
Decision Trees
Ensemble the predictions 


6) Your challenges and successes
The biggest challenge is imputing income. Have achieved relative success imputing with KNN regressor, however, I’d like to run a more sophisticated model and also clean income which are off by 1000s.

7) Possible extensions or business applications of your project
- N/A - yet

8) Conclusions and key learnings
Importance of having good, high quality data
careful examination of data before using models
putting a lot of thought into feature selection. 

