import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


## Import Dataset
Active_Hands = pd.read_csv('Active_Hands.csv',index_col= 'username')
Ball_Handling_In_Motion = pd.read_csv('Ball_Handling_In_Motion.csv',index_col= 'username')
Footwork1 = pd.read_csv('Footwork1.csv',index_col= 'username')
Footwork2 = pd.read_csv('Footwork2.csv',index_col= 'username')
Help_And_Recover = pd.read_csv('Help_And_Recover.csv',index_col= 'username')
Kick_Slide_Run_Defense = pd.read_csv('Kick_Slide_Run_Defense.csv',index_col= 'username')
Rip_First_Step = pd.read_csv('Rip_First_Step.csv',index_col= 'username')
Static_Ball_Handling = pd.read_csv('Static_Ball_Handling.csv',index_col= 'username')

## Concatenate datasets 
scores = pd.concat([Active_Hands, Ball_Handling_In_Motion,Footwork1,Footwork2 ,
                    Kick_Slide_Run_Defense,Rip_First_Step ,Static_Ball_Handling,Help_And_Recover], axis=1).sort_values('status')

## Split target
X = scores.iloc[:, 0:-1].values
y = scores.iloc[:, -1].values


## Label Encode the target 
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

## Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify = y)

## Training XGBoost on the Training set
from xgboost import XGBClassifier
classifier = XGBClassifier()
classifier.fit(X_train, y_train)

## Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
y_pred = classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
print('accuracy score:', accuracy_score(y_test, y_pred))

## Compare pred to y_test
compare =  np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1)
print(compare)

## Applying k-Fold Cross Validation
from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 5)
print("Accuracy k fold: {:.2f} %".format(accuracies.mean()*100))
print("Standard Deviation k fold: {:.2f} %".format(accuracies.std()*100))

