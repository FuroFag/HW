import numpy as np 
from sklearn import datasets 
from sklearn.svm import SVR 
from sklearn.metrics import mean_squared_error, explained_variance_score 
from sklearn.utils import shuffle 
from sklearn.datasets import fetch_california_housing
import pandas as pd
import numpy as np

# Загрузка данных с ценами на жилье 
data = datasets.load_breast_cancer() 
# Перемешивание данных 
X, y = shuffle(data.data, data.target, random_state=7)
# Разбивка данных на обучающий и тестовый наборы 
num_training = int(0.8 * len(X)) 
X_train, y_train = X[:num_training], y[:num_training] 
X_test, y_test = X[num_training:], y[num_training:] 
# Создание регрессионной модели на основе SVM 
sv_regressor = SVR(kernel='linear', C=1.0, epsilon=0.1) 
# Обучение регрессора SVМ 
sv_regressor.fit(X_train, y_train)
# Оценка эффективности работы регрессора 
y_test_pred = sv_regressor.predict(X_test) 
mse = mean_squared_error(y_test, y_test_pred) 
evs = explained_variance_score(y_test, y_test_pred)  
print("\n#### Оценка эффективности ####") 
print("Среднеквадратическая ошибка =", round(mse, 2)) 
print("Explained variance score =", round(evs, 2))
# Тестирование регрессора на тестовой точке данных 
test_data = [3.7, 0, 18.4, 1, 0.87, 5.95, 91, 2.5052, 26, 666, 20.2, 351.34, 15.27, 22, 13.11, 2, 3, 3, 3, 6, 1.12, 2.21, 0.92, 1.01, 11.11, 4.12, 5.32, 2, 0, 1] 
print("\nPredicted price:", sv_regressor.predict([test_data])[0]) 

