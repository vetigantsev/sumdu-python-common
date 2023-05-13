# Перший студент має розмістити текст обсягом до 100 слів
# і написати програмний код обробки тексту,
# застосувавши щонайменше три вбудовані функції Python для обробки рядків.
# Програмний код має супроводжуватися коментарями із поясненням.
#
# Усі студенти повинні працювати з текстом, який розмістив перший студент.
# Кожен студент у відповіді на завдання для спільної роботи окрім посилання на програмний код
# розміщує короткий опис функцій, які він застосував, та зазначає три функції,
# які потрібно застосувати до цього тексту наступному студенту.
#
# Окремі функції по роботі з текстом можуть повторюватися,
# але кожен студент має використати щонайменше дві нові функції.
#
# У результаті виконання завдань усіма студентами має бути один програмний код,
# у якому у коментарях до частин програмного коду вказати прізвища студентів, які їх писали.

text = """ В Путивлі-граді вранці-рано
    Співає, плаче Ярославна,
    Як та зозуленька кує,
    Словами жалю додає.
    «Полечу,— каже,— зигзицею ,
    Тією чайкою-вдовицею,
    Та понад Доном полечу,
    Рукав бобровий омочу
    В ріці Каялі. І на тілі,
    На княжім білім, помарнілім,
    Омию кров суху, отру
    Глибокії, тяжкії рани...»
    
    І квилить, плаче Ярославна
    В Путивлі рано на валу:
    «Вітрило-вітре мій єдиний,
    Легкий, крилатий господине!
    Нащо на дужому крилі
    На вої любії мої,
    На князя, ладо моє миле,
    Ти ханові метаєш стріли?
    Не мало неба, і землі,
    І моря синього. На морі
    Гойдай насади-кораблі.
    А ти, прелютий... Горе! Горе!
    Моє веселіє украв,
    В степу на тирсі розібгав»."""

words = {
    "Ярославна": "Святославна",
    "кує": "гуде",
    "чайкою": "качкою",
    "плаче": "квилить",
    "крилатий": "шляхетний",
    "любії": "ніжнії",
}


def task3():
    # KarinaChernobai start

    global text
    # виводимо на екран довжину рядка
    print("Char count:", len(text))
    # виводимо на екран кількість слів у тексті, використовуємо split для розбиття рядка на слова
    print("Word count:", len(text.split()))
    # змінюємо одні слова на інші у тексті, використовуючи словник words, результат виводимо на екран
    mod_text = text
    for key, value in words.items():
        mod_text = mod_text.replace(key, value)
    print(mod_text)

    # KarinaChernobai end

    # три функції, які потрібно застосувати до цього тексту наступному студенту:
    # S [i:j:step]
    # S.find (str, [start], [end]) 
    # S.swapcase()

    return
