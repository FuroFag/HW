from sklearn.cluster import AffinityPropagation
from sklearn import metrics
# from sklearn.datasets.samples_generator import make_blobs
from sklearn.datasets import make_blobs
# Формирование выборки
centers = [[1, 1], [-1, -1], [1, -1]]
n_samples, cluster_std, preference = 190, 0.9, -170
X, labels_true = make_blobs(n_samples=n_samples, centers=centers, cluster_std=cluster_std, random_state=0)

# Вычисление распространения сходства
af = AffinityPropagation(preference=preference).fit(X)
cluster_centers_indices = af.cluster_centers_indices_
labels = af.labels_

n_clusters_ = len(cluster_centers_indices)

print('Оценка числа кластеров: %d' % n_clusters_)
print("Однородность: %0.3f" % metrics.homogeneity_score(labels_true, labels))
print("Полнота: %0.3f" % metrics.completeness_score(labels_true, labels))
print("V-measure: %0.3f" % metrics.v_measure_score(labels_true, labels))
print("Adjusted Rand Index: %0.3f"% metrics.adjusted_rand_score(labels_true, labels))
print("Adjusted Mutual Information: %0.3f"% metrics.adjusted_mutual_info_score(labels_true, labels, average_method='arithmetic'))
print("Силуэтный коэффициент: %0.3f"% metrics.silhouette_score(X, labels, metric='sqeuclidean'))

# Визуализация результатов
import matplotlib.pyplot as plt
from itertools import cycle
plt.close('all')
plt.figure(1)
plt.clf()

colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
 class_members = labels == k
 cluster_center = X[cluster_centers_indices[k]]
 plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
 plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=14)
 for x in X[class_members]:
  plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)
plt.title('Оценочное число кластеров: %d' % n_clusters_)
plt.show()

