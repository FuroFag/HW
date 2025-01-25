import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def target_function(x, y):
    return np.sin(np.sqrt(x**2 + y**2))  # Пример целевой функции

def read_data_from_file(file_path):
    data = np.loadtxt(file_path, delimiter=',')
    return data

def plot_surface(data, threshold):
    x = data[:, 0]
    y = data[:, 1]
    
    # Создаем сетку для X и Y
    X = np.linspace(min(x), max(x), 100)
    Y = np.linspace(min(y), max(y), 100)
    X, Y = np.meshgrid(X, Y)
    
    # Вычисляем Z значения по целевой функции
    Z = target_function(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.7)  # Создаем поверхность

    # Добавляем плоскость значений
    Z_threshold = np.full(X.shape, threshold)  # Плоскость значений
    ax.plot_surface(X, Y, Z_threshold, color='r', alpha=0.5)  # Плоскость заданного значения

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.set_title('3D Surface Visualization of Data')
    plt.show()

    return Z, Z_threshold

def calculate_intersection_area(Z, Z_threshold):
    # Вычисляем площадь соприкосновения
    intersection = (Z <= Z_threshold)  # Логическая матрица соприкосновения
    area = np.sum(intersection)  # Считаем количество точек соприкосновения
    total_points = Z.size  # Общее количество точек

    # Вычисляем оптимальное значение на базе точек соприкосновения
    if area > 0:
        optimal_value = np.mean(Z[intersection])  # Среднее значение точек соприкосновения
    else:
        optimal_value = None  # Если нет точек соприкосновения

    return area, total_points, optimal_value

# Основной код
file_path = 'data.txt'  # Путь к текстовому файлу с данными
threshold = 0.5  # Значение, с которым будет сравниваться плоскость
data = read_data_from_file(file_path)  # Чтение данных
Z, Z_threshold = plot_surface(data, threshold)  # Визуализация данных

# Вычисление площади соприкосновения
area, total_points, optimal_value = calculate_intersection_area(Z, Z_threshold)

# Вывод результатов
percentage = (area / total_points) * 100
print(f"Площадь соприкосновения: {area} точек из {total_points} ({percentage:.2f}%)")
if optimal_value is not None:
    print(f"Оптимальное значение на базе точек соприкосновения: {optimal_value:.4f}")
else:
    print("Нет точек соприкосновения для вычисления оптимального значения.")
