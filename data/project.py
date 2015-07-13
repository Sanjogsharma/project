import pandas as pd
import matplotlib.pyplot as plot
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import train_test_split
import numpy as np


user_cols = ['dlq' , 'total_lines', 'age', 'past_30', 'debtratio', 
             'income', 'credit_lines', 'past_90', 'home_lines',
             'past_60', 'dep_count']
             
#read the data in console and created new header name
training = pd.read_table('cs-training.csv', sep=',', header=False,\
 names=user_cols)
#read file, changed index, changed names
 
test = pd.read_table('cs-test.csv', sep = ',', header=False,\
names=user_cols)

#same as line 12
sns.heatmap(training.corr())
#dlq and age have negative correlation, past due dates and  dlq have
#positive correlation
feature_cols= training.iloc[:, 1:10]

sns.pairplot(training, x_vars=['age', 'past_30', 'past_90',\
             'past_60'], y_vars='dlq', kind='reg')

# all the N/As in the age column are filled. 



#validating, train a knn model on those features, with income as response/ 
# and do a predict on X> most correlated
#knn regression > average of nearest neighbors. 

#to do it really well: treat it as it own regression problem 
#100k split into test/train > evaluate and tune


# What happened to NaNs?
training.dep_count.fillna(value=0, inplace=True)
training_imp = training.dropna()  

from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.cross_validation import train_test_split
knn = KNeighborsClassifier(n_neighbors=50000)
yi = training_imp.income
Xi = training_imp[['total_lines', 'age', 'past_30', 'debtratio', 
             'credit_lines', 'past_90', 'home_lines',
             'past_60', 'dep_count']]

Xi_train, Xi_test, yi_train, yi_test = train_test_split(Xi, yi, \
test_size=0.4, random_state=4)


knn.fit(Xi_train, yi_train)

yi_pred = knn.predict(Xi_test)
print metrics.accuracy_score(yi_test, yi_pred)









####################LOGISTICAL REFGRESSION
X = training[['total_lines', 'age', 'past_30', 'debtratio', 
             'income', 'credit_lines', 'past_90', 'home_lines',
             'past_60', 'dep_count']]
y = training.dlq


# What happened to NaNs?
training.dep_count.fillna(value=0, inplace=True)






#impute zero
#argue imputing 1 b/c 
#knn - with knn; set up a series of rules

#kaggle 