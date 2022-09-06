## Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

## Import Dataset
data = pd.read_csv('Ex6_Footwork.csv',index_col= 'username')

X = data.drop(['status'],axis=1)

## Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)


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
kmeans = KMeans(n_clusters=3,init='k-means++', n_init=20)   #best k=5
y_kmeans = kmeans.fit_predict(X)

df = pd.DataFrame(data)
df['y_kmeans'] = y_kmeans

## Create a table to compare y_kmeans results with the status (pro,athlete,noob) of users
compare = df[['status','y_kmeans']]
compare.sort_values('y_kmeans',inplace=True)

# accuracy=22/30
# print(accuracy)

## Set score depending on cluster (0,1, or 2)
Footwork2 = []
for name in compare.index:
    if ( (name=='ΛΑΖΟΣ ΛΑΜΠΡΟΥ') | (name=='ΣΠΥΡΟΣ ΟΙΚΟΝΟΜΟΥ') | (name=='ΑΛΕΞΑΝΔΡΟΣ ΕΥΘΥΜΙΟΥ') | (name=='ΙΩΑΝΝΗΣ ΜΠΕΛΛΟΣ')):
        
        Footwork2.append(0)
        
    elif ((name=='ΚΩΣΤΑΝΤΙΝΟΣ ΗΛΙΑΔΗΣ') | (name=='ΔΙΑΜΑΝΤΗΣ ΤΣΙΤΩΝΗΣ')  | (name=='ΑΛΕΞΑΝΔΡΟΣ ΕΥΘΥΜΙΟΥ')  | (name=='ΛΑΖΟΣ ΛΑΜΠΡΟΥ')  |
          (name=='ΣΠΥΡΟΣ ΟΙΚΟΝΟΜΟΥ') | (name=='ΚΩΣΤΑΣ ΣΠΥΡΙΚΟΣ') | (name=='ΚΩΣΤΑΣ ΜΠΕΛΛΟΣ')  | (name=='ΙΩΑΝΝΗΣ ΜΠΟΤΣΑΡΗΣ')  |
          (name=='ΒΙΚΤΩΡΑΣ ΘΕΙΑΚΟΣ')  |  (name=='ΑΛΕΞΑΝΔΡΟΣ ΠΡΕΜΕΤΗΣ') | (name=='ΧΡΗΣΤΟΣ ΜΠΟΤΣΑΡΗΣ') |
          (name=='ΔΗΜΗΤΡΗΣ ΔΕΡΤΙΜΑΝΗΣ')  | (name=='ΘΩΜΑΣ ΠΑΠΑΔΙΩΤΗΣ')):
         
        Footwork2.append(1)
        
    else:
        Footwork2.append(2)
    
    
compare['Footwork2'] = Footwork2

## Find out if clusters make sense   
compare['mean_response'] = data['mean_response']

mean_0 = compare[compare['Footwork2'] == 0]['mean_response'].mean()
mean_1 = compare[compare['Footwork2'] == 1]['mean_response'].mean()
mean_2 = compare[compare['Footwork2'] == 2]['mean_response'].mean()


print("cluster 0 mean_response:", mean_0)
print("cluster 1 mean_response:", mean_1)
print("cluster 2 mean_response:", mean_2)

## Export the scores of the exercise
Footwork2 = compare["Footwork2"]

Footwork2.to_csv('Footwork2.csv')