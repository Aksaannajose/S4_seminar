from datetime import datetime
from re import X

import inline
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbours import KNeighborsClassifier



data = pd.read_csv('sat.csv')
data.info()
data.head()


sns.pairplot(data, x_vars = ['X', 'Y', 'time'], y_vars = 'wind_speed')
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 1)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X,y)

timestamp = 42368.149155
#convert timestamp to datetime object
dt_object = datetime.fromtimestamp(timestamp)
print("dt_object:", dt_object)

from datetime import datetime
timestamp = 1627112345
#convert timestamp to datetime object
curr_time = datetime.fromtimestamp(timestamp)
print("Current Time:", curr_time)

data['Time_Analysis'] = pd.to_datetime(data['time'], unit='s')

data.head()

y_pred = knn.predict(X)
print(metrics.accuracy_score(y,y_pred))

