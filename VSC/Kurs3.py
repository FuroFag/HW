import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression  # Используем логистическую регрессию для классификации
from sklearn.metrics import classification_report, confusion_matrix

# Загрузка данных
data = np.loadtxt('data.txt', delimiter=',', dtype=str)

# Извлечение признаков и целевой переменной
X = data[:, :-1]  # Все столбцы, кроме последнего
y = data[:, -1]   # Последний столбец (целевой переменной)

# Кодируем категориальные переменные
label_encoders = {}
for i in range(X.shape[1]):
    if np.issubdtype(X[:, i].dtype, np.object_):
        le = LabelEncoder()
        X[:, i] = le.fit_transform(X[:, i])
        label_encoders[i] = le

# Разделяем данные на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Масштабируем данные
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train.astype(float))
X_test = scaler.transform(X_test.astype(float))

# Кодируем целевую переменную
y_encoder = LabelEncoder()
y_train = y_encoder.fit_transform(y_train)
y_test = y_encoder.transform(y_test)

# Создаем и обучаем классификатор (логистическая регрессия для бинарной классификации)
classifier = LogisticRegression()
classifier.fit(X_train, y_train)

# Предсказание
y_pred = classifier.predict(X_test)

# Оценка модели
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
