from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")
import csv


dataset = pd.read_csv('College.csv')
x = dataset.iloc[:,[2,3,4,5,6,7,8]]    #This  loads column specific data from the dataset
#print(x)
y = dataset.iloc[:5]
#print(y)

#Prints how many samples we have of each label( so App, Category...)
#print(dataset["Category"].value_counts())

from sklearn import preprocessing
scaler = preprocessing.StandardScaler()
scaler.fit(x)
X_scaled_array = scaler.transform(x)
X_scaled = pd.DataFrame(X_scaled_array, columns=x.columns)



#Elbow Method for knowing number of clusters
wcss = []
for i in range(1,17):
   kmeans = KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=17,random_state=2)
   kmeans.fit(x)
   wcss.append(kmeans.inertia_)

plt.plot(range(1,17))
plt.title('The Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('Wcss')
plt.show()

from sklearn.metrics import silhouette_score

x = dataset.iloc[:,[2,3,4,5,6,7,8]]

silhouette_score(x , labels=17, metric='euclidean', sample_size=None, random_state=None)








print('Done')