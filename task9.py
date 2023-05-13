# Виконати обробку природомовного тексту англійською мовою,
# записаного у текстовому файлі, для його подальшого використання в задачах NLP.
#
# Перший студент має створити текстовий файл, у який записати природомовний текст
# з 200 слів англійською мовою з якогось літературного твору.
# Програмно реалізувати дві задачі з обробки тексту - наприклад, токенізація
# та видалення стоп-слів і написати, які дві задачі реалізовувати наступному студенту.
# Кожну задачу реалізовувати в окремій функції користувача.
#
# Задачею усіх студентів є провести обробку цього тексту та визначити його відтінок -
# positive, negative чи neutral (Sentiment Analysis за допомогою бібліотеки NLTK).
#
# Якщо усі задачі було реалізовано попередніми студентами,
# студенту потрібно протестувати роботу готової програми на іншому тексті
# та запропонувати удосконалення окремих модулів програми, щонайменше двох.
# У програмному коді коментарі обов'язкові.

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

file_path = r'docs/task9.txt'


# функція для обробки тексту
def preprocess_text(text):
    # KarinaChernobai start

    # токенізація тексту
    tokens = word_tokenize(text)
    # видалення стоп слів
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]

    # KarinaChernobai end

    # завдання для наступного студента:
    # видалення знаків пунктуації
    # лематизація токенів

    processed_text = ' '.join(filtered_tokens)
    return processed_text


# функція, яка визначає відтінок тексту
def sentiment_scores(text):
    sid_obj = SentimentIntensityAnalyzer()
    # a sentiment dictionary, which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(text)

    print("Sentiment dictionary: ", sentiment_dict)
    print("Text was rated as", sentiment_dict['neg'] * 100, "% negative.")
    print("Text was rated as", sentiment_dict['neu'] * 100, "% neutral.")
    print("Text was rated as", sentiment_dict['pos'] * 100, "% positive.")

    print("Overall text was rated as", end=" ")
    if sentiment_dict['compound'] >= 0.05:
        print("positive.")
    elif sentiment_dict['compound'] <= - 0.05:
        print("negative.")
    else:
        print("neutral.")


def task9():
    # KarinaChernobai start

    try:
        # відкриваємо файл
        with open(file_path, 'r', encoding='utf-8') as f:
            # зчитуємо дані
            data = f.readlines()
            mod_text = preprocess_text(''.join(data))
            sentiment_scores(mod_text)
    except FileNotFoundError as e:
        # обробляємо помилки
        print(f"File {e.filename} cannot be opened.")

    # KarinaChernobai end

    return
