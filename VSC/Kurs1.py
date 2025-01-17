import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Шаг 1: Загрузка данных из текстового файла с использованием numpy
data = np.loadtxt('data.txt', delimiter=',', dtype=str)

# Шаг 2: Разделение данных на текст и метки
X = data[:, 0]  # Текстовые данные
y = data[:, 1]  # Метки классов

# Шаг 3: Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Шаг 4: Создание наивного байесовского классификатора
model = make_pipeline(CountVectorizer(), MultinomialNB())

# Шаг 5: Обучение модели
model.fit(X_train, y_train)

# Шаг 6: Оценка модели
accuracy = model.score(X_test, y_test)
print(f'Accuracy: {accuracy:.2f}')

# Шаг 7: Применение модели для предсказания
sample_text = ["пример текста для классификации"]
predicted = model.predict(sample_text)
print(f'Predicted class: {predicted[0]}')