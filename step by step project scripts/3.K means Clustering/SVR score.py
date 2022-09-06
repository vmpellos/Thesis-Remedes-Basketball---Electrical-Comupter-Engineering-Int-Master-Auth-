## Import Libraries
import pandas as pd
import numpy as np



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
scores = pd.concat([Active_Hands, Ball_Handling_In_Motion, Static_Ball_Handling, Footwork1, 
                    Kick_Slide_Run_Defense, Footwork2, Rip_First_Step, Help_And_Recover], axis=1).sort_values('status')

## Split target
X = scores.iloc[:, 0:-1].values
y = scores.iloc[:, -1].values

## Label Encode the target 
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

# ## Splitting the dataset into the Training set and Test set
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify = y)

## Training the SVR model on the whole dataset
from sklearn.svm import SVR
svr = SVR(kernel = 'rbf')
svr.fit(X,y)

## Predictig Results for X_test
pred = svr.predict(X)
# print('pred of X_test',pred)


## Compare pred to y_test
compare =  np.concatenate((pred.reshape(len(pred),1), y.reshape(len(y),1)),1)
print("Compare pred to y_test")
print(compare)

## Evalute model with r2 score
from sklearn.metrics import r2_score
r2score = r2_score(y, pred)
print('R2 SCORE:',r2score)


## Evalute model with RMSE & MSE & MAE
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from math import sqrt
mse = mean_squared_error(y,pred)
rmse = sqrt(mean_squared_error(y,pred))
mae = mean_absolute_error(y,pred)
from sklearn.metrics import f1_score
f1score = f1_score(y,pred.round() ,average='micro')
print('F1 SCORE:',f1score)
print('MSE:',mse)
print('RMSE:',rmse)
print('MAE:',mae)


## Applying Grid Search to find the best model and the best parameters
from sklearn.model_selection import GridSearchCV
parameters = [{'C': [0.25, 0.5, 0.75, 1], 'kernel': ['linear']},
              {'C': [0.25, 0.5, 0.75, 1], 'kernel': ['rbf'], 'gamma': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]},
              {'C': [0.25, 0.5, 0.75, 1], 'kernel': ['poly'], 'gamma': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]},
              {'C': [0.25, 0.5, 0.75, 1], 'kernel': ['sigmoid'], 'gamma': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]}]
grid_search = GridSearchCV(estimator = svr,
                           param_grid = parameters,
                           scoring = 'r2',
                           cv = 10,
                           n_jobs = -1)
grid_search.fit(X, y)
best_R2 = grid_search.best_score_
best_parameters = grid_search.best_params_
print("Best R2: {:.2f} %".format(best_R2*100))
print("Best Parameters:", best_parameters)


## Save model
import pickle
with open("area_model.pickle", "wb") as file:
    pickle.dump(svr, file)