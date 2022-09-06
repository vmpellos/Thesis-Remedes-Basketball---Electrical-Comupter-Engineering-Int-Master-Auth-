## Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Import Dataset
data = pd.read_csv('Ex1_ActiveHands.csv',index_col= 'username')

X = data.drop('status',axis=1)

# ## Feature Scaling
# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler()
# X = sc.fit_transform(X)



## Using the elbow method to find optimal number of clusters
from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters=i,init='k-means++', n_init=20)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11),wcss)
plt.title('The elbow method')
plt.xlabel('number of clusters')
plt.ylabel('wcss')
plt.show()



## Training the K-Means model on the dataser
kmeans = KMeans(n_clusters=3,init='k-means++')
y_kmeans = kmeans.fit_predict(X)

df = pd.DataFrame(data)
df['y_kmeans'] = y_kmeans

## Create a table to compare y_kmeans results with the status (pro,athlete,noob) of users
compare = df[['status','y_kmeans']]
compare.sort_values('y_kmeans',inplace=True)

# accuracy=19/30
# print(accuracy)

## Set score depending on cluster (0,1, or 2)
Active_Hands = []
for name in compare.index:
    if ((name=='ΑΓΓΕΛΟΣ ΡΕΦΑΤΛΛΑΡΗ') | (name=='ΚΩΣΤΑΝΤΙΝΟΣ ΗΛΙΑΔΗΣ') | (name=='ΧΑΡΗΣ ΣΙΑΝΑΣ') | (name=='ΘΩΜΑΣ ΠΑΠΑΔΙΩΤΗΣ') | 
        (name=='ΔΗΜΗΤΡΗΣ ΔΕΡΤΙΜΑΝΗΣ') | (name=='ΓΙΩΡΓΟΣ ΝΙΚΟΠΟΥΛΟΣ') | (name=='ΙΩΑΝΝΗΣ ΜΠΕΛΛΟΣ') | (name=='ΑΛΕΞΑΝΔΡΟΣ ΤΣΙΤΟΣ') |
        (name=='ΒΑΣΙΛΗΣ ΜΠΟΤΣΑΡΗΣ') | (name=='ΑΛΕΞΑΝΔΡΟΣ ΠΡΕΜΕΤΗΣ')):
        
        Active_Hands.append(1)
        
    elif ((name=='ΒΙΚΤΩΡΑΣ ΘΕΙΑΚΟΣ') | (name=='ΠΑΣΧΑΛΗΣ ΠΑΠΑΝΙΚΟΛΑΟΥ') | (name=='ΠΑΡΗΣ ΘΩΜΟΣ') | (name=='ΝΙΚΟΣ ΠΑΠΑΔΟΠΟΥΛΟΣ') | 
        (name=='ΚΡΙΤΩΝΑΣ ΤΖΙΜΑΣ') | (name=='ΧΡΗΣΤΟΣ ΜΠΟΤΣΑΡΗΣ') | (name=='ΑΛΕΞΑΝΔΡΟΣ ΘΕΙΑΚΟΣ') | (name=='ΘΟΔΩΡΗΣ ΤΣΙΡΩΝΗΣ') |
        (name=='ΗΛΙΑΣ ΜΠΑΤΖΙΟΣ') | (name=='ΒΑΣΙΛΕΙΟΣ ΜΠΕΛΛΟΣ')):
        
        Active_Hands.append(2)
        
    else:
        Active_Hands.append(0)
    
    
compare['Active_Hands'] = Active_Hands

## Find out if clusters make sense
compare['mean_response'] = data['mean_response']
compare['dm_errors'] = data['dm_errors']

mean_0 = compare[compare['Active_Hands'] == 0][['mean_response',"dm_errors"]].mean()
mean_1 = compare[compare['Active_Hands'] == 1][['mean_response',"dm_errors"]].mean()
mean_2 = compare[compare['Active_Hands'] == 2][['mean_response',"dm_errors"]].mean()

print("cluster 0:")
print(mean_0)
print("cluster 1:")
print(mean_1)
print("cluster 2:")
print(mean_2)

## Export the scores of the exercise
active_hands = pd.DataFrame(compare["Active_Hands"])
active_hands.to_csv('Active_Hands.csv')