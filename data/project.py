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
sns.heatmap(test.corr())
feature_cols= training.iloc[:, 1:10]

sns.pairplot(training, x_vars=['age', 'past_30', 'past_90',\
             'past_60'], y_vars='dlq', kind='reg')

X = training[['total_lines', 'age', 'past_30', 'debtratio', 
             'income', 'credit_lines', 'past_90', 'home_lines',
             'past_60', 'dep_count']]
y = training.dlq

null_default = training.dlq.mean()

# What happened to NaNs?
X_train, X_test, y_train, y_test = train_test_split(X, y, \
test_size=0.3, random_state=1)


default = LogisticRegression()
default.fit(X_train, y_train)
B1 = default.coef_[0][0]
B0 = default.intercept_[0]
np.exp(B1)

y_pred = default.predict(X_test)

