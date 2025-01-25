import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import MeanShift, estimate_bandwidth

# Загрузка данных из входного файла
input_file = 'sales.csv'
file_reader = csv.reader(open(input_file, 'r'), delimiter= ',')
X = []
for count, row in enumerate(file_reader):
  if not count:
    names = row[1:]
    continue
  X.append([float(x) for x in row[1:]])

# Преобразование данных в массив numpy
Х = np.array(X)

# Оценка ширины окна входных данных
bandwidth = estimate_bandwidth(X, quantile=0.99, n_samples=len(X))

# Вычисление кластеризации методом сдвига среднего
meanshift_model = MeanShift(bandwidth=bandwidth, bin_seeding=True)
meanshift_model.fit(X)

labels = meanshift_model.labels_
cluster_centers = meanshift_model.cluster_centers_
num_clusters = len(np.unique(labels))

print("\nNumber of clusters in input data =", num_clusters)
print("\nCenters of clusters:")
print('\t'.join([name[:3] for name in names]))
for cluster_center in cluster_centers:
 print('\t' .join([str(int(x)) for x in cluster_center]))

# Извлечение двух признаков в целях визуализации
cluster_centers_2d = cluster_centers[:, 1:3]

# Отображение центров кластеров
plt.figure()
plt.scatter(cluster_centers_2d[:, 0], cluster_centers_2d[:, 1], s=120, edgecolors='black', facecolors='none')
offset = 0.25

# Использование np.ptp для вычисления диапазона
plt.xlim(cluster_centers_2d[:, 0].min() - offset * np.ptp(cluster_centers_2d[:, 0]),
         cluster_centers_2d[:, 0].max() + offset * np.ptp(cluster_centers_2d[:, 0]))

plt.ylim(cluster_centers_2d[:, 1].min() - offset * np.ptp(cluster_centers_2d[:, 1]),
         cluster_centers_2d[:, 1].max() + offset * np.ptp(cluster_centers_2d[:, 1]))

plt.title('Цeнтpы 2D-кластеров')
plt.show()
