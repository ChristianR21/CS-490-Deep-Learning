#Christian Rodas
#This program shows the difference when using the SVM with the RBF kernal



#Modules
import csv
from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA


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

#Gets the iris.csv data
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


flowers = datasets.load_iris()
X = flowers.data[:, :2]
y = flowers.target

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

plt.figure(2, figsize=(8, 6))
plt.clf()

# Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1,
            edgecolor='k')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

# To getter a better understanding of interaction of the dimensions
# plot the first three PCA dimensions
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
X_reduced = PCA(n_components=3).fit_transform(flowers.data)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=y,
           cmap=plt.cm.Set1, edgecolor='k', s=40)
ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])






from sklearn.svm import SVC

#X = flowers[['sepal length', 'sepal width', 'petal length', 'petal width']]
#y = flowers['class']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)   #this trains the test data using sklearn.model_selection module

svm = SVC()
svm.fit(X_train, y_train)

#print(X_train)
print('Accuracy of SVM classifier on training set: {:.2f}'
     .format(svm.score(X_train, y_train)))
print('Accuracy of SVM classifier on test set: {:.2f}'
     .format(svm.score(X_test, y_test)))

print("Finished")
#plt.show() #When on, its very slow to print the svm classifer score

#Conclusion:
#Using the SVM with RBF kernal yeild different results because RBF kernals are
#for smoothing, which doesn't make sense for text data, thus the accuracy drop