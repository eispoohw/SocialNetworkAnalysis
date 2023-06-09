# Исследование социального графа, расчёт его характеристик
## Ход работы

Можно использовать один из графов, полученных в ходе предыдущей работы, или создать новый. Добавьте изображение графа в отчёт. Данная работа посвящена исследованию социального графа посредством вычисления различных метрик. Некоторые метрики были затронуты в предыдущей работе и не дублируются в этой, поэтому в случае создания нового графа повторите также пункты 6 и 7 из лабораторной работы №1. 

1. **Найдите наиболее авторитетных пользователей**

В качестве метрики авторитетности пользователя используйте центральность - число минимальных кратчайших путей между любыми двумя его “друзьями” или “собеседниками”, проходящих через него.

1. **Вычислите плотность социального графа**

Плотность графа - это отношение реального числа связей в графе к максимально возможному в неориентированном графе с тем же числом вершин.

1. **Является ли граф связным? Что это означает применительно к исследуемому социальному графу?**

Связный граф - граф, содержащий ровно одну компоненту связности. Это означает, что между любой парой вершин этого графа существует как минимум один путь.

1. **Рассчитайте максимальное, минимальное и среднее значение степени узлов графа**
2. **Рассчитайте модулярность графа**

Модулярность - это скалярная величина из отрезка [−1, 1], которая количественно описывает неформальное определение структуры сообществ.