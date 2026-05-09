# Проект FitLife - MVP версия 1.0
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

WATER_PER_KG = 30  # Стандартная рекомендация.
ML_PER_L = 1000  # Количество мл. в л..
FLINE = ('-') * 40

print(
    'Добро пожаловать в FitLife! ',
    'Я Ваш персональный помощник на пути к здоровой жизни.',
)
user_name = input(
    'Давайте знакомиться, '
    'мое имя Фил, а Ваше?'
)
print(f'Приятно познакомиться, {user_name}!')

while True:
    try:
        user_age = int(input('Подскажите Ваш возраст?'))
        break
    except ValueError:
        print('Попробуйте еще раз, введите число.')

while True:
    try:
        user_weight = float(input('Ваш вес (в кг)?'))
        break
    except ValueError:
        print('Попробуйте еще раз, введите число.')

while True:
    try:
        user_height = float(input(
            'Ваш рост (введите рост в метрах, '
            'используя точку: 1.87)? '))
        break
    except ValueError:
        print('Пожалуйста, введите корректное число.')

print()
print(
    'Отлично! Первым делом, узнаем Ваш ИМТ ',
    '(Индекс массы тела) и норму приема воды.',
)
bmi = user_weight / (user_height ** 2)
# Рассчитаываем индекс массы тела.

water_nedded_ml = user_weight * WATER_PER_KG
# Затем норму воды в день.
water_nedded_l = water_nedded_ml / ML_PER_L  # Переводим в литры.
# ИМТ и норму воды ограничиваем одним знаком после запятой,
# для удобства пользователя.
print(FLINE)
print(
    f'Отчет для пользоватателя: {user_name} ({user_age} г.)\n',
    f'Ваш вес: {user_weight} кг.\n',
    f'Ваш рост: {user_height} м.\n',
    f'Ваш ИМТ: {round(bmi, 1)}\n',
    f'Рекомендуемая норма воды: {round(water_nedded_l, 1)} л. в день',
)
print(FLINE)
print("Расчет окончен. Будьте здоровы!")
