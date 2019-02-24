from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns
#sns.set(style="white", color_codes=True)
import warnings
warnings.filterwarnings("ignore")
import csv
from sklearn.svm import SVC

from sklearn import metrics
from sklearn.cluster import KMeans


#Reads in data and combines them
train_df=pd.read_csv('train.csv')
test_df=pd.read_csv('test.csv')
combine =[train_df, test_df]


dataset = pd.read_csv('train.csv')
# see how many samples we have of each species
print(dataset["Sex"].value_counts())

#sns = Library, FacetGrid= method (dataset= data loaded, hue=what are the labels/features, size= size of graph
#bins=graphical numerical orientation
sns.FacetGrid(dataset, hue="Sex", size=6) \
   .map(plt.hist, "Survived", bins=20) \
   .add_legend()
plt.show()

#Yes because the number female who survived were much higher than the males, even with the fact that there
#more males than females.


#Shows statistics of values
# train_df.info()
# test_df.info()

#Prints those that survived 1=survived 0=died
print(train_df['Survived'].value_counts(dropna='False'))

#Prints the null values which is good for determining what features to drop
#print(train_df.isnull().sum())

train_df["Embarked"] = train_df["Embarked"].fillna("S")
train_df.drop("Cabin", axis=1,inplace=True)         #This drops values so cabin in this case
test_df.drop("Cabin", axis=1, inplace=True)
#train_df.drop("PassengerId", axis=1,inplace=True)   #Dropping passengerid since won't affect whoe died/survived
#test_df.drop("PassengerId", axis=1, inplace=True)
# train_df.drop("Name", axis=1, inplace=True)         #Name won't have any affect on survival
# test_df.drop("Name", axis=1, inplace=True)
# train_df.drop("Ticket", axis=1, inplace=True)         #Name won't have any affect on survival
# test_df.drop("Ticket", axis=1, inplace=True)

combine =[train_df, test_df]


# #After features are dropped
# print("After dropped")
# train_df.info()
# test_df.info()


train_df[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived', ascending=False)



#Converts Sex to a new feature called gender
for dataset in combine:
    dataset['Sex'] =dataset['Sex'].map( {'female': 1, 'male': 0} ).astype(int)


#prints a histogram plot
#sns.FacetGrid(train_df, col='Survived').plot('hist')

# g =sns.FacetGrid(train_df, col='Survived')
# print(g)
# g.map(plt.g, 'Age',  bins=20)
#g = sns.FacetGrid(train_df, col="Survived")
#g = g.map(plt.scatter, "Pclass", "Survived", bins='auto', color='b')



print("done")








#
# # train_df= pd.read_csv('train.csv')
# # test_df= pd.read_csv('test.csv')
# # X_train= train_df.drop("Survived",axis=1)
# # Y_train= train_df["Survived"]
# # X_test= test_df.drop("PassengerId",axis=1).copy()
# # print(train_df[train_df.isnull().any(axis=1)])
#
#
# X_train = train_df("Survived", axis=1)
# Y_train = train_df.drop("Survived", axis=1)
# X_test = test_df.drop["Gender"]
#
#
#
# svc = SVC()
# svc.fit(X_train, Y_train)
# Y_pred= svc.predict(X_test)
# acc_svc= round(svc.score(X_train, Y_train) * 100, 2)
# print("svm accuracy is:", acc_svc)



