#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mom', 'dad', 'grandmother']

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['mom', 173],
    ['dad', 175],
    ['grandmother', 169]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Dad height ', my_family_height[1][1])
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
print('Sum height ', my_family_height[0][1] + my_family_height[1][1] + my_family_height[2][1])
