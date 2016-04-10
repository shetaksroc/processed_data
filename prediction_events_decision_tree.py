import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import csv
from sklearn.externals import joblib
rf=joblib.load('decision_events/m1.pkl')
cols = ['event_id', 'lat', 'long', 'y','x','weekno','weekday','hr','min'] 
colsRes = ['pixel']
#with open('model/m1', 'wb') as f:
 #   cPickle.dump(rf, f)
test = pd.read_csv("bishop.csv")
testArr = test.as_matrix(cols)
results = rf.predict(testArr)
# something I like to do is to add it back to the data frame, so I can compare side-by-side
#test['predictions'] = results
#test.head()
#result_f = open('result.txt', 'a')
for i in results:
	print(i)