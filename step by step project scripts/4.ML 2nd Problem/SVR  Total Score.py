## Import Libraries
import pandas as pd
import numpy as np
import pickle

## Import Dataset
Active_Hands = pd.read_csv('pred1.csv',index_col= 'username')
Ball_Handling_In_Motion = pd.read_csv('pred2.csv',index_col= 'username')
Static_Ball_Handling = pd.read_csv('pred3.csv',index_col= 'username')
Quick_Feet = pd.read_csv('pred4.csv',index_col= 'username')
Kick_Slide_Run_Defense = pd.read_csv('pred5.csv',index_col= 'username')
Footwork = pd.read_csv('pred6.csv',index_col= 'username')
Rip_First_Step = pd.read_csv('pred7.csv',index_col= 'username')
Help_And_Recover = pd.read_csv('pred8.csv',index_col= 'username')

svr_scores = pd.concat([Active_Hands,Ball_Handling_In_Motion,Static_Ball_Handling,Quick_Feet
                        ,Kick_Slide_Run_Defense,Footwork,Rip_First_Step,Help_And_Recover],axis=1)


# ## Import Dataset
# Active_Hands = pd.read_csv('predictions1.csv',index_col= 'username')
# Ball_Handling_In_Motion = pd.read_csv('predictions2.csv',index_col= 'username')
# Static_Ball_Handling = pd.read_csv('predictions3.csv',index_col= 'username')
# Quick_Feet = pd.read_csv('predictions4.csv',index_col= 'username')
# Kick_Slide_Run_Defense = pd.read_csv('predictions5.csv',index_col= 'username')
# Footwork = pd.read_csv('predictions6.csv',index_col= 'username')
# Rip_First_Step = pd.read_csv('predictions7.csv',index_col= 'username')
# Help_And_Recover = pd.read_csv('predictions8.csv',index_col= 'username')

# svr_scores = pd.concat([Active_Hands,Ball_Handling_In_Motion,Static_Ball_Handling,Quick_Feet
#                         ,Kick_Slide_Run_Defense,Footwork,Rip_First_Step,Help_And_Recover],axis=1)


## Create the status column
status = []
for name in svr_scores.index:
    if ((name =='ΙΩΑΝΝΗΣ ΜΠΕΛΛΟΣ') | (name =='ΣΠΥΡΟΣ ΟΙΚΟΝΟΜΟΥ') | (name =='ΛΑΖΟΣ ΛΑΜΠΡΟΥ') | (name =='ΚΩΣΤΑΣ ΜΠΕΛΛΟΣ') | (name =='ΚΩΣΤΑΝΤΙΝΟΣ ΗΛΙΑΔΗΣ') |
        (name =='ΙΩΑΝΝΗΣ ΜΠΟΤΣΑΡΗΣ') | (name =='ΔΙΑΜΑΝΤΗΣ ΤΣΙΤΩΝΗΣ') | (name =='ΧΡΗΣΤΟΣ ΜΠΟΤΣΑΡΗΣ') | (name =='ΑΛΕΞΑΝΔΡΟΣ ΕΥΘΥΜΙΟΥ') | (name =='ΑΛΕΞΑΝΔΡΟΣ ΠΡΕΜΕΤΗΣ')):
        status.append(0)
    elif ((name =='ΑΛΕΞΑΝΔΡΟΣ ΤΣΙΤΟΣ') | (name =='ΔΗΜΗΤΡΗΣ ΔΕΡΤΙΜΑΝΗΣ') | (name =='ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ') | (name =='ΗΛΙΑΣ ΜΠΑΤΖΙΟΣ') | (name =='ΣΠΥΡΟΣ ΠΕΤΣΗΣ') |
        (name =='ΘΩΜΑΣ ΠΑΠΑΔΙΩΤΗΣ') | (name =='ΧΑΡΗΣ ΣΙΑΝΑΣ') | (name =='ΚΩΝ ΠΑΠΑΝΙΚΟΛΑΟΥ') | (name =='ΒΙΚΤΩΡΑΣ ΘΕΙΑΚΟΣ') | (name =='ΚΩΣΤΑΣ ΣΠΥΡΙΚΟΣ')):
        status.append(1)
    else:
        status.append(2)
        
svr_scores['status'] = status

## Split target
X = svr_scores.iloc[:, 0:-1].values
y = svr_scores.iloc[:, -1].values

# X = svr_scores.drop('status',axis=1)
# y = svr_scores['status']


## Import Trained model "svr"
with open('area_model.pickle', "rb") as file:
    svr = pickle.load(file)
    

## Predict Results of X
predict_final_score = svr.predict(X)

## Compare "predict_final_score" to y_test
compare =  np.concatenate((predict_final_score.reshape(len(predict_final_score),1), y.reshape(len(y),1)),1)
print("Compare predictions to y")
print(compare)


## Evalute model with r2 score
from sklearn.metrics import r2_score
r2score = r2_score(y, predict_final_score)
print('R2 SCORE:',r2score)


## Evalute model with F1 score

predict_final_score = pd.DataFrame(predict_final_score)
from sklearn.metrics import f1_score
f1score = f1_score(y, round(predict_final_score),average='micro')
print('F1 SCORE:',f1score)