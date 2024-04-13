import math
from pygame_init import font, surface, pg


def calculate_points(start, end, length, num_points):
    """Функция получения координат точек на отрезке"""
    # Расчет шага между точками
    step = length / (num_points - 1)

    # Извлечение координат начала и конца отрезка
    x1, y1 = start
    x2, y2 = end

    # Создание списка для хранения координат точек
    points = []

    # Расчет координат для каждой точки
    for i in range(num_points):
        # Вычисление текущей позиции
        current_position = i * step

        # Расчет координат точки на отрезке
        x = x1 + current_position * (x2 - x1) / length
        y = y1 + current_position * (y2 - y1) / length

        # Добавление координат в список
        points.append((x, y))

    return points


def get_position_of_arrow(r, clock_dict, center, clock_hand):
    """Функция получения конечных координат для отрезка выходящего из центра
    принимает на вход словарь значений углов для каждого числа из 60"""
    wight, height = center
    x = wight + r * math.cos(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    y = height + r * math.sin(math.radians(clock_dict[clock_hand]) - math.pi / 2)
    return x, y


def draw_arrow(points, clock_value):
    """Функция отрисовки стрелок из чисел"""
    for point in points:
        hour_arrow_text = font.render(clock_value, True, pg.Color("#000451"))
        surface.blit(source=hour_arrow_text, dest=point)
        pass
    pass
