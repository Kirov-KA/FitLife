# Проект FitLife - MVP версия 1.0
WATER_PER_KG = 30

# 1. Знакомство
# Имя пользователя
user_name = input('Ваше имя? ')
user_name = user_name.title()
# Возраст пользователя
while True:
    try:
        user_age = int(input('Сколько вам полных лет? '))
        break
    except ValueError:
        print('Пожалуйста, введите число!')

# 2. Сбор данных
# Вес пользователя (в кг)
while True:
    try:
        user_weight = float(input('Ваш вес (в кг)? '))
        user_weight = round(user_weight, 1)
        break
    except ValueError:
        print('Пожалуйста, введите число!')

# Рост пользователя (в метрах, например 1.75)
while True:
    try:
        user_height = float(input('Ваш рост (в метрах, например 1.75)? '))
        user_height = round(user_height, 2)
        break
    except ValueError:
        print('Пожалуйста, укажите число с разделителем точка!')


# 3. Расчет индекса массы тела
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

# Подсчет воды: вес * 30 мл
water_ml = user_weight * float(WATER_PER_KG)
water_l = water_ml / 1000
water_l = round(water_l, 1)

# 4. Вывод красивого результата
# Приветствие пользователя
print(f'\nПривет, {user_name}!\n')
# Данные о здоровье пользователя
print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l} л. в день\n')
print('Расчет окончен. Будьте здоровы!')
