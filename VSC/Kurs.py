import numpy as np 
from sklearn import preprocessing
from tkinter import *

#Задание №1. Предобработка данных. Автор: Иванов И.И.

#Входные данные
input_data_1 = np.array([[12, 15, 14, 10, 8],
                        [22, 18, 20, 25, 30],
                        [5, 7, 9, 6, 4],
                        [18, 20, 15, 22, 19],
                        [30, 28, 25, 27, 29]])

input_data_2 = np.array([[3, 7, 5, 11, 13],
                        [14, 9, 6, 8, 12],
                        [10, 15, 17, 4, 2],
                        [1, 0, 3, 6, 5],
                        [19, 22, 21, 20, 18]])

input_data_3 = [['a', 4], ['b', 6], ['c', 3], ['d', 8], ['e', 5]]



#Обработка
def button_clicked_1():
    print('\nВходные данные:')
    print(input_data_1)
    print('\nСтандартизованные данные набор_1:')
    input_data_1_scaled = preprocessing.scale(input_data_1)
    print(input_data_1_scaled)
    scaler = preprocessing.StandardScaler().fit(input_data_1)
    print('\nСтандартизованные данные набор_2 (StandardScaler):')
    print(scaler.transform(input_data_2))
    print('\nСтандартизованные данные набор_1 (MinMaxScaler):')
    min_max_scaler = preprocessing.MinMaxScaler()
    input_data_1_minmax = min_max_scaler.fit_transform(input_data_1)
    print(input_data_1_minmax)
    print('\nСтандартизованные данные набор_1 (MaxAbsScaler):')
    max_abs_scaler = preprocessing.MaxAbsScaler()
    input_data_1_maxabs = max_abs_scaler.fit_transform(input_data_1)
    print(input_data_1_maxabs)
    print('\nНормализованные данные набор_1 (Ll-нормализация):')
    data_normalized_l1 = preprocessing.normalize(input_data_1, norm='l1')
    print(data_normalized_l1)
    print('\nНормализованные данные набор_1 (L2-нормализация):')
    data_normalized_l2 = preprocessing.normalize(input_data_1, norm='l2')
    print(data_normalized_l2)
    print('\nКодированные данные набор_3 (OrdinalEncoder):')
    enc = preprocessing.OrdinalEncoder()
    print(enc.fit(input_data_3))
    print(enc.categories_)
    print(enc.transform(input_data_3))
    
def button_clicked_2():    
    print('\nДискретизация данных набор_1:')
    diskr = preprocessing.KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='uniform')
    diskr.fit(input_data_1)
    input_data_1_diskr = diskr.transform(input_data_1)
    print(input_data_1_diskr)

def button_clicked_3():    
    print('\nБизаризация данных набор_1:')
    input_data_1_binarized = preprocessing.Binarizer(threshold=11.2).transform(input_data_1) 
    print(input_data_1_binarized)

def button_clicked_4():
    print('\nВходные данные:')
    print(input_data_2)
    print('\nСтандартизованные данные набор_2:')
    input_data_2_scaled = preprocessing.scale(input_data_2)
    print(input_data_2_scaled)
    scaler = preprocessing.StandardScaler().fit(input_data_2)
    print('\nСтандартизованные данные набор_2 (StandardScaler):')
    print(scaler.transform(input_data_2))
    print('\nСтандартизованные данные набор_2 (MinMaxScaler):')
    min_max_scaler = preprocessing.MinMaxScaler()
    input_data_2_minmax = min_max_scaler.fit_transform(input_data_2)
    print(input_data_2_minmax)
    print('\nСтандартизованные данные набор_2 (MaxAbsScaler):')
    max_abs_scaler = preprocessing.MaxAbsScaler()
    input_data_2_maxabs = max_abs_scaler.fit_transform(input_data_2)
    print(input_data_2_maxabs)
    print('\nНормализованные данные набор_2 (Ll-нормализация):')
    data_normalized_l1 = preprocessing.normalize(input_data_2, norm='l1')
    print(data_normalized_l1)
    print('\nНормализованные данные набор_2 (L2-нормализация):')
    data_normalized_l2 = preprocessing.normalize(input_data_2, norm='l2')
    print(data_normalized_l2)
    print('\nКодированные данные набор_2 (OrdinalEncoder):')
    enc = preprocessing.OrdinalEncoder()
    print(enc.fit(input_data_3))
    print(enc.categories_)
    print(enc.transform(input_data_3))

def button_clicked_5():
    print('\nДискретизация данных набор_2:')
    diskr = preprocessing.KBinsDiscretizer(n_bins=8, encode='ordinal', strategy='uniform')
    diskr.fit(input_data_2)
    input_data_2_diskr = diskr.transform(input_data_2)
    print(input_data_2_diskr)

def button_clicked_6():
    print('\nБизаризация данных набор_2:')
    input_data_2_binarized = preprocessing.Binarizer(threshold=2.1).transform(input_data_2) 
    print(input_data_2_binarized)
        
root=Tk()
button1 = Button(root, text="Предобработка", command=button_clicked_1)
button1.pack()
button2 = Button(root, text="Дискретизация", command=button_clicked_2)
button2.pack()
button3 = Button(root, text="Бинаризация", command=button_clicked_3)
button3.pack()
button1_2 = Button(root, text='Предобработка набора 2', command = button_clicked_4)
button1_2.pack()
button2_2 = Button(root, text = 'Дискретизация набора 2', command = button_clicked_5)
button2_2.pack()
button3_2 = Button(root, text = 'Бинаризация набора 2', command = button_clicked_6)
button3_2.pack()
root.mainloop()