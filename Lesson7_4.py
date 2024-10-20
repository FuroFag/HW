print('В команде Мастера кода участников: %s' % str(5))
team1_num = 5
team2_num = 6
print('Итого сегодня в командах участников %(team1_num)s и %(team2_num)s' %{'team1_num': 5, 'team2_num': 6})
score_1 = 40
score_2 = 42
print('Команда Волшебники данных решила задач: {}'.format(score_2))
team1_time = 11015.223
team2_time = 12332
print('Волшебники данных решили задачи за {} c!'.format(team1_time))
print(f'Команды решили {score_1} и {score_2} задач')
tasks_total = score_1 + score_2
time_avg = 350.4
if score_1 > score_2:
    print('Результат битвы: победа команды Мастера кода!')
else:
    print('Результат битвы: победа команды Волшебники данных')
print(f'Сегодня было решено {tasks_total} задач, в среднем за {time_avg} секунды на задачу!')

