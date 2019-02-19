#Christian Rodas
#This is program is to implement Gaussian NB's method and model selection
#to evaulate a model

#First find the the number of mislabeled points using the GuassianNB method
#then read in the data. So, in this case its the iris.csv file
#With that data, it plot the points.
#Following that, the data is seperated into "train" and "test" groups
#Then we implement the cross validation(model selection) and output the accuracy
#Finally we output the plot



#Modules
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split    #No longer .cross_validatoin... now its model_selection
from sklearn import datasets
from sklearn.naive_bayes import GaussianNB




#This function gets the values from the csv file
import csv


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


iris = datasets.load_iris()
X = iris.data[:, :150]
y = iris.target

x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5

plt.figure(2, figsize=(8, 6))
plt.clf()





#Plot the training points
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Set1,
            edgecolor='k')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())


# To getter a better understanding of interaction of the dimensions
#plot the first three PCA dimensions
fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=110)
X_reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(X_reduced[:, 0], X_reduced[:, 1], X_reduced[:, 2], c=y,
           cmap=plt.cm.Set1, edgecolor='k', s=40)
ax.set_title("First three PCA directions")
ax.set_xlabel("1st eigenvector")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("2nd eigenvector")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("3rd eigenvector")
ax.w_zaxis.set_ticklabels([])


#This code implements the Gaussian Naive Bayes method
gnb = GaussianNB()
y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
print("Number of mislabeled points out of a total %d points : %d" % (iris.data.shape[0],(iris.target != y_pred).sum())) ;


plt.show()


# getting the data and response of the dataset
x = iris.data
y = iris.target

#Tests the data and splits
#This code implements the cross validation(model selection) which splits the data into "test" and "train" data
#This is to prevent it from being too baised or have too variance
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

#This code implements the K neighors, puts a new data pt to the category with the most neighbors
model = KNeighborsClassifier(n_neighbors=5)
model.fit(x_train, y_train)

#Predictor
y_pred = model.predict(x_test)

print("Metric accuracy score:",metrics.accuracy_score(y_test, y_pred))

k_range = range(1, 20)
scores = []



for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    scores.append(metrics.accuracy_score(y_test, y_pred))

import matplotlib.pyplot as plt



plt.plot(k_range, scores)
plt.xlabel("value of k")
plt.ylabel("testing accuracy")

plt.show()


