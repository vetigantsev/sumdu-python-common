# Перший студент має створити словник, в якому має зберігатися інформація про успішність студентів групи, а саме:
# номер групи;
# прізвище, ім'я та по батькові;
# курс;
# предмети та оцінки за семестр.
#
# Окрім обов'язкових елементів словника можна додавати власні.
#
# Також перший студент має написати програмний код, у якому реалізувати одну із функцій по роботі зі словником -
# наприклад, додавання даних.
#
# Усі студенти повинні працювати зі словником, який розмістив перший студент.
# У програмному коді коментарі обов'язкові.
#
# У результаті виконання завдань усіма студентами має бути один програмний код,
# у якому у коментарях до частин програмного коду вказати прізвища студентів, які їх писали.

class Student:
    def __init__(self, Age, Course, Group):
        self.Age = Age
        self.Course = Course
        self.Group = Group


students = {
    'Maxim Olegovich Komarov': Student(20, 'Accounting', 11),
    'Regina Johnson': Student(19, 'Liberal Arts', 12),
    'Carol Stevenson': Student(21, 'Education', 4),
    'Maria Jefferson': Student(18, 'Mathematics', 5),
    'John Adams': Student(21, 'Acting', 8),
    'Rob Erikson': Student(22, 'Accounting', 11),
}


def print_students():
    for key, value in students.items():
        print('\033[1m', key, '\033[0m')
        print("вік:", value.Age)
        print("курс:", value.Course)
        print("група:", value.Group)
        print()


def task5():
    # KarinaChernobai start

    # виведемо на екран створений на початку словник
    print("Початковий словник")
    print_students()
    # додамо запис про нову студентку у словник
    students["Claudia Edelstein"] = Student(18, "Mathematics", 14)
    # видалимо запис про студента зі словника
    del students['Maxim Olegovich Komarov']
    # виведемо на екран словник зі змінами
    print("Словник з внесеними змінами")
    print_students()

    # KarinaChernobai end

    # наступний студент може, наприклад, відсортувати словник
    return
