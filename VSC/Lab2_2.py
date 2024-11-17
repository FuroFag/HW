import numpy as np 
from sklearn import linear_model  
import matplotlib.pyplot as plt 
from Lab2_3 import visualize_classifier


from sklearn.naive_bayes import GaussianNB  
from sklearn.model_selection import train_test_split, cross_val_score 
from utilities import visualize_classifier
#from utilities import visualize_classifier
# Определение образца входных данных 
X = np.array([[3, 4.2], [4, 6.7], [2.9, 8], [5.1, 4.5], [6, 5], [5.6, 5], [3.3, 0.4], [3.9, 0.9], [2.8, 1], 
[0.5, 5.2], [1.1, 3.2], [1.6, 4.9]]) 
y = np.array([1, 1, 2, 1, 1, 1, 2, 2, 2, 3, 3, 3])
# Создание логистического классификатора 
classifier = linear_model.LogisticRegression(solver='liblinear', C=12)
# Тренировка классификатора 
classifier.fit(X, y)
# Визуализация работы классификатора 
visualize_classifier(classifier, X, y)
# Разбивка данных на обучающий и тестовый наборы 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3) 
classifier_new = GaussianNB() 
classifier_new.fit(X_train, y_train) 
y_test_pred = classifier_new.predict(X_test)
# Вычисление правильности классификатора 
accuracy = 100.0 * (y_test == y_test_pred).sum() / X_test.shape[0] 
print("Accuracy of the new classifier =", round(accuracy, 2), "%") 
# Визуализация работы классификатора 
visualize_classifier(classifier_new, X_test, y_test)

num_folds = 3 
accuracy_values = cross_val_score(classifier,  X, y, scoring='accuracy', cv=num_folds) 
print("Accuracy: " + str(round(100*accuracy_values.mean(), 2)) + "%") 
precision_values = cross_val_score (classifier,  X, y, scoring='precision_weighted', cv=num_folds) 
print("Precision: " + str(round(100*precision_values.mean(), 2)) + "%") 
recall_values = cross_val_score (classifier,  X, y, scoring='recall_weighted', cv=num_folds) 
print("Recall: " + str(round(100*recall_values.mean(), 2)) + "%") 
f1_values = cross_val_score (classifier,  X, y, scoring='f1_weighted', cv=num_folds) 
print("F1: " + str(round(100*f1_values.mean(), 2)) + "%")