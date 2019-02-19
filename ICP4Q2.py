#Christian Rodas
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


#This function gets the values from the csv file
def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)  # skipping column names
        i = 0;
        for row in csvFileReader:
            #print(', '.join(row))
            i += 1
            #print("row num:", i)
            #print(row)
    return

get_data('iris.csv') ;

flowers = pd.read_csv('iris.csv')
#print(eyes) #prints the pandas dataframe of the iris.csv file

#print(eyes['eye_name'].unique())   #This should print the unique columns but doensnt
print(flowers.describe())  #This prints the statistical information of the data

#What this does is that it shows a graph and the number of values/items that each one goes to
#So for example, there are 50 of each iris class
import seaborn as sns
sns.countplot(flowers['petal width'],label="Count")     #to change what to plot its in the []

#Plots a graph with the data
#plt.show() #When on its very slow to print the svm classifer

from sklearn.svm import SVC

X = flowers[['sepal length', 'sepal width', 'petal length', 'petal width']]
y = flowers['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)   #this trains the test data using sklearn.model_selection module

svm = SVC()
svm.fit(X_train, y_train)
print('Accuracy of SVM classifier on training set: {:.2f}'
     .format(svm.score(X_train, y_train)))
print('Accuracy of SVM classifier on test set: {:.2f}'
     .format(svm.score(X_test, y_test)))

print("Finished")
