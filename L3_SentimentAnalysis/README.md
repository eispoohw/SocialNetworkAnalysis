На практике анализ текстовых данных в социальных сетях может быть полезен для целого ряда задач. К примеру, можно
распознавать токсичные посты для их модерации или анализировать тональность текста, чтобы оценить отношение группы людей
к тому или иному явлению. В этой лабораторной работе мы будем исследовать пользовательские посты, посвящённые COVID-19

## Ход работы

**1. Скачайте набор данных Covid 19 Indian Sentiments on covid19 and lockdown по ссылке**

[Covid 19 Indian Sentiments on covid19 and lockdown](https://www.kaggle.com/datasets/surajkum1198/twitterdata)

С его помощью мы будем обучать модель распознавать настроение автора поста.

2. **В датафрейме оставьте только те строки, у которых в столбце `sentiment` написано sad и joy**

Для простоты выполнения оставляем только 2 возможных настроения, строки с постами, не соответствующими им, можно
удалить.

3. **Примените на этом наборе данных шаги предварительной обработки**

К шагам предварительной обработки относятся:

1. приведение к нижнему регистру,
2. токенизация,
3. удаление стоп-слов (обратите внимание на то, что стоп-слова должны соответствовать языку, с которым ведётся работа, в
   данном случае это английский),
4. уберите заведомо неинформативные данные (хэштеги и отметки пользователей).

Также необходимо произвести векторизацию.

Пример выполнения этих шагов на другом наборе можно подсмотреть здесь:

[Google Colaboratory](https://colab.research.google.com/drive/14dcDHynxOyhb510HO2lmsoFmBSLO5Vfx?usp=sharing)

Чтобы улучшить качество обучения можно попробовать перед векторизацией также применить лемматизацию (приведение слов к
исходной форме). Для этого подойдёт, к примеру, nltk.WordNetLemmatizer (pymorphy2).

4. **Обучите классификатор**

Можно использовать реализацию из библиотеки Scikit-learn

```python
# импорт классификатора
from sklearn.naive_bayes import MultinomialNB

clf = MultinomialNB()
# обучаем с помощью векторизованной обучающей выборки
clf.fit(vectorized_x_train, y_train)
# импорт метрик качества
from sklearn.metrics import *

# получаем предсказание для векторизованной тестовой выборки
pred = clf.predict(vectorized_x_test)
# сравниваем реальные метки с предсказанными
print(classification_report(y_test, pred))
```

5. **Оцените качество классификации. Обучите еще одну или несколько классический моделей классификаторов и сравните
   качество. Подберите наиболее оптимальные гиперпараметры векторизатора и классификатора, при которых метрики будут
   выше.**

[Google Colaboratory](https://colab.research.google.com/drive/1mmZ2M0r4J-IYGJ3pNDHfProhd5qtij_N?usp=sharing)

6. **Примените шаги предобработки на наборе данных COVID19 Tweets**

[COVID19 Tweets](https://www.kaggle.com/datasets/gpreda/covid19-tweets)

7. **С помощью обученного классификатора найдите посты из набора данных COVID19 Tweets, которые можно отнести к классу
   sad. Какой процент от общего количества постов они составляют?**
8. **Проанализируйте тональность постов из набора данных COVID19 Tweets с помощью библиотеки TextBlob (Dostoevsky*).
   Какое процентное соотношение постов разных настроений наблюдается?**