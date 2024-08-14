grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sorted = sorted(students)
st_n_gr = dict(zip(students_sorted, grades))
print (st_n_gr)

Aaron_Grades = sum(st_n_gr['Aaron']) / len(st_n_gr['Aaron'])
Bilbo_Grades = sum(st_n_gr['Bilbo']) / len(st_n_gr['Bilbo'])
Johnny_Grades = sum(st_n_gr['Johnny']) / len(st_n_gr['Johnny'])
Khendrick_Grades = sum(st_n_gr['Khendrik']) / len(st_n_gr['Khendrik'])
Steve_Grades = sum(st_n_gr['Steve']) / len(st_n_gr['Steve'])
st_n_gr['Aaron'] = Aaron_Grades
st_n_gr['Bilbo'] = Bilbo_Grades
st_n_gr['Johnny'] = Johnny_Grades
st_n_gr['Khendrik'] = Khendrick_Grades
st_n_gr['Steve'] = Steve_Grades
print(st_n_gr)


