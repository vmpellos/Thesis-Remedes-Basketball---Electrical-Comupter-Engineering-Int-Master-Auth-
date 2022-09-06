## Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Importing the dataset
Ex4_QuickFeet = pd.read_csv('Ex4_QuickFeet.csv', index_col='username')
# Ex4_QuickFeet.drop(['template_name'],axis=1,inplace=True)

# X = Ex4_QuickFeet.iloc[:, 0:-1].values
# y = Ex4_QuickFeet.iloc[:, -1].values
X = Ex4_QuickFeet.drop('status',axis=1)
y= Ex4_QuickFeet['status']


## Label Encode the target 
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)

## Plot a heat map to identify important corellations 
Ex4 = X
Ex4['status'] = y
sns.heatmap(Ex4[['mean_response','successes%','dm_errors','status']].corr(),cmap='coolwarm',annot=True, linewidth=0.5)
# plt.figure(figsize = (16,5))
# sns.heatmap(Ex3.corr(),cmap='coolwarm',annot=True, linewidth=0.5)
plt.title("Ex4_QuickFeet", fontsize =20)


## Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, stratify = y, random_state=11)


# ## Feature Scaling
# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)

# print(Ex4_QuickFeet)
# print(X_train)
# print("\n")
# print(X_test)


## Training the SVR model on the whole dataset
from sklearn.svm import SVR
svr = SVR(kernel = 'linear', C=0.5)
svr.fit(X_train,y_train)

## Predictig Results for X_test
pred = svr.predict(X_test)
# print('pred of X_test',pred)

## Compare pred to y_test
compare =  np.concatenate((pred.reshape(len(pred),1), y_test.reshape(len(y_test),1)),1)
print("Compare pred to y_test")
print(compare)

## Evalute model with r2 score
from sklearn.metrics import r2_score
r2score = r2_score(y_test,pred)
print('R2 SCORE:',r2score)

## Evalute model with RMSE & MSE & MAE
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from math import sqrt
mse = mean_squared_error(y_test,pred)
rmse = sqrt(mean_squared_error(y_test,pred))
mae = mean_absolute_error(y_test,pred)
from sklearn.metrics import f1_score
f1score = f1_score(y_test,pred.round() ,average='micro')
print('F1 SCORE:',f1score)
print('MSE:',mse)
print('RMSE:',rmse)
print('MAE:',mae)


## Applying k-Fold Cross Validation
from sklearn.model_selection import cross_val_score
R2 = cross_val_score(estimator = svr, X = X_train, y = y_train, cv = 10, scoring='r2')
MSE= cross_val_score(estimator = svr, X = X_train, y = y_train, cv = 10, scoring='neg_mean_squared_error')
RMSE= cross_val_score(estimator = svr, X = X_train, y = y_train, cv = 10, scoring='neg_root_mean_squared_error')
MAE= cross_val_score(estimator = svr, X = X_train, y = y_train, cv = 10, scoring='neg_mean_absolute_error')
print("R2 mean: {:.2f} %".format(R2.mean()*100))
print("MSE mean: {:.2f} %".format(MSE.mean()*100))
print("RMSE mean: {:.2f} %".format(RMSE.mean()*100))
print("MAE mean: {:.2f} %".format(MAE.mean()*100))
# print("Standard Deviation: {:.2f} %".format(R2.std()*100))

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
grid_search.fit(X_train, y_train)
best_R2 = grid_search.best_score_
best_parameters = grid_search.best_params_
print("Best R2: {:.2f} %".format(best_R2*100))
print("Best Parameters:", best_parameters)


## Export preds
X_test['pred'] = pred
pred4 = X_test['pred']
X_test.drop('pred', axis=1, inplace=True)

pred4.to_csv('pred4.csv')

## Predict score for all users
predictions = svr.predict(X)
compare =  np.concatenate((predictions.reshape(len(predictions),1), y.reshape(len(y),1)),1)
print("Compare pred to y_test")
print(compare)

## Export preds
X['predictions'] = predictions
predictions4 = X['predictions']
X.drop('predictions', axis=1, inplace=True)
predictions4.to_csv('predictions4.csv')
