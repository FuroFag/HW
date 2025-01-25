import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import KMeans

# Загрузка данных из входного файла
X = np.loadtxt('data_quality.txt', delimiter=',')

# Включение входных данных в график
plt.figure()
plt.scatter(X[:,0], X[:,1], marker='o', facecolors='none', edgecolors='black', s=80)
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
plt.title('Входные данные')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())

# Инициализация переменных
scores = []
values = np.arange(6, 14)

# Итерирование в определённом диапазоне значений
for num_clusters in values:
 # Обучение модели кластеризации КМеаns
 kmeans = KMeans(init='k-means++', n_clusters=num_clusters, n_init=10)
 kmeans.fit(X)
 # Получить силуэтную оценку
 score = metrics.silhouette_score(X, kmeans.labels_, metric='euclidean', sample_size=len(X))

 print("\nКоличество кластеров =", num_clusters)
 print("Силуэтная оценка =", score)
    
 scores.append(score)

# Отображение силуэтных оценок на графике
plt.figure()
plt.bar(values, scores, width=0.7, color='black', align='center')
plt.title('Силуэтная оценка числа кластеров')
          
# Извлечение наилучшей оценки и оптимального количества кластеров
num_clusters = np.argmax(scores) + values[0]
print('\nОптимальное количество кластеров =', num_clusters)
plt.show()

