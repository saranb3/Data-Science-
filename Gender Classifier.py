from sklearn import tree 
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC


#[height, weight, shoe size] 
X = [[180,80,44], [170,70,43], [160,60,38], [150,50,35], [170,70,40], [ 175,64,39], [180,80,44], [170,70,43], [160,60,38], [150,50,35], [170,70,40], [ 175,64,39]]

#matches with list in X
Y = ['male', 'male', 'female', 'female', 'female', 'male', 'female', 'male', 'male', 'male', 'female', 'female']

#task we have a bunch of data and we want to predict the gender of a new person
#we can loop through all the classifiers and see which one is the best

models = [tree.DecisionTreeClassifier(), RandomForestClassifier(), MLPClassifier(), SVC()]
for clf in models: 
    clf.fit(X,Y)
    prediction = clf.predict([[150, 90, 43], [150,50,20]])
    print(prediction)


