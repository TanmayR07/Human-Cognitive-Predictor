
import pickle

import numpy as np  # Fundamental package for linear algebra and multidimensional arrays
import pandas as pd  # Data analysis and manipultion tool

# In read_csv() function, we have passed the location to where the files are located in the dphi official github page.
train_data = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/hippocorpus/train_set_label.csv" )

X = train_data.drop(['recAgnPairId','recImgPairId','similarityReason','story','WorkerId','AssignmentId','summary',
            'annotatorRace','mainEvent','mostSurprising','memType'],axis = 1)
y = train_data['memType'] # Output/Dependent variable

Gender = X.annotatorGender
Gender_final = []
for item in Gender:
    if item == 'Man' or item == 'man' or item == 'MAN':
        Gender_final.append(0)
    elif item == 'woman' or item == 'WOMAN' or item == 'Woman':
        Gender_final.append(1)
    else:
        Gender_final.append(2)

X.drop('annotatorGender',axis = 1, inplace = True)
X['Gender'] = Gender_final

distracted_text = X.distracted

distarcted_final = []
for item in distracted_text:
    if item == 'one':
        distarcted_final.append(1)
    elif item == '2.0':
        distarcted_final.append(2)
    elif item == '3.0':
        distarcted_final.append(3)
    elif item == '4.0':
        distarcted_final.append(4)        
    else:
        distarcted_final.append(5)

X.drop('distracted',axis = 1, inplace = True)
X['distracted_num']  = distarcted_final

draining_text = X.draining

draining_final = []
for item in draining_text:
    if item == 'one':
        draining_final.append(1)
    elif item == '2.0':
        draining_final.append(2)
    elif item == '3.0':
        draining_final.append(3)
    elif item == '4.0':
        draining_final.append(4)        
    else:
        draining_final.append(5)

X.drop('draining',axis = 1, inplace = True)
X['draining']  = draining_final

y_enc = []
for item in y:
    if item == 'recalled':
        y_enc.append(0)
    elif item == 'imagined':
        y_enc.append(1)
    else:
        y_enc.append(2)
y_enc     
#y = np.array(y_enc)

# import train_test_split
from sklearn.model_selection import train_test_split

X_train, X_val, y_train, y_val = train_test_split(X,y,test_size=0.3, random_state = 42)

X_train.annotatorAge.fillna(X_train.annotatorAge.mean(), inplace=True)
X_train.importance.fillna(X_train.importance.mean(), inplace=True)
X_train.frequency.fillna(X_train.frequency.mean(), inplace=True)
X_train.similarity.fillna(X_train.similarity.mean(), inplace=True)

X_val.annotatorAge.fillna(X_val.annotatorAge.mean(), inplace=True)
X_val.importance.fillna(X_val.importance.mean(), inplace=True)
X_val.frequency.fillna(X_val.frequency.mean(), inplace=True)
X_val.similarity.fillna(X_val.similarity.mean(), inplace=True)

from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
X_train = ss.fit_transform(X_train)
X_val = ss.fit_transform(X_val)

params = {"max_depth": [25],
               "min_samples_split": [3],
              "min_samples_leaf": [1,2,3],
              "bootstrap": [True],
              "n_estimators": [125],
                 "n_jobs": [-1],
             "verbose": [2],
            "criterion": ["entropy"]
         }

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

rfc1 = RandomForestClassifier()
clf = GridSearchCV(rfc1, params,cv = 4)
clf.fit(X_train,y_train)

pred_clf = clf.predict(X_val)

from sklearn.metrics import f1_score

result = clf.score(X_val, y_val)
print('The Score is;', result)

print('F1 Score for random forest classifier is: ', f1_score(y_val, pred_clf, average = 'weighted'))

#save the model 
filename = 'model.pkl'
pickle.dump(clf, open(filename, 'wb'))
