import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Функция для чтения данных из файла
def read_data_from_file(file_path):
    data = np.genfromtxt(file_path, delimiter=',', skip_header=1)  # Чтение данных из CSV
    return data

# Функция для подготовки данных
def prepare_data(data, target_index):
    X = np.delete(data, target_index, axis=1)  # Признаки
    y = data[:, target_index]  # Целевая переменная
    return X, y

# Функция для визуализации результатов
def plot_results(y_true, y_pred):
    plt.figure(figsize=(10, 6))
    sns.countplot(x=y_true, label='True', alpha=0.5)
    sns.countplot(x=y_pred, label='Predicted', alpha=0.5)
    plt.title('True vs Predicted Labels')
    plt.xlabel('Labels')
    plt.ylabel('Count')
    plt.legend()
    plt.show()

# Основной код
file_path = 'data.txt'  # Путь к файлу с данными
target_index = -1  # Индекс столбца с целевой переменной (последний столбец)

# Чтение данных
data = read_data_from_file(file_path)

# Подготовка данных
X, y = prepare_data(data, target_index)

# Разделение данных на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=20)

# Создание и обучение модели наивного байесовского классификатора
model = GaussianNB()
model.fit(X_train, y_train)

# Прогнозирование на тестовой выборке
y_pred = model.predict(X_test)

# Оценка модели
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Вывод результатов
print(f'Accuracy: {accuracy:.4f}')
print('Classification Report:')
print(report)

# Визуализация результатов
plot_results(y_test, y_pred)
