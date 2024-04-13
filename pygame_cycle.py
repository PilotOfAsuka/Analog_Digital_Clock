from vars import *
from pygame_init import *
from func import *
from datetime import datetime
from random import randint


def pygame_cycle(run=False):
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

        # Заливка фона
        surface.fill(pg.Color("#E2AE86"))
        # Получение времени
        current_time = datetime.now()
        hours, minutes, seconds = (((current_time.hour % 12) * 5 + current_time.minute // 12),
                                   current_time.minute, current_time.second)

        # Отрисовка меток циферблата
        for digit, pos in clock60.items():
            radius = 10 if not digit % 3 and not digit % 5 else 5 if digit % 5 else 2
            pg.draw.circle(surface, pg.Color("#103C13"), get_position_of_arrow(r=300, center=CENTER_CIRCLE,
                                                                               clock_hand=digit,
                                                                               clock_dict=clock60), radius)
            pass

        # Координаты точек на секундной стрелки для отрисовки чисел_стрелок
        points_for_second_arrow = calculate_points(CENTER, get_position_of_arrow(r=length_arrow,
                                                                                 center=CENTER, clock_dict=clock60,
                                                                                 clock_hand=seconds),
                                                   length_arrow, NUM_OF_POINTS)

        # Координаты точек на секундной стрелки для отрисовки чисел_стрелок
        points_for_minute_arrow = calculate_points(CENTER, get_position_of_arrow(r=length_arrow,
                                                                                 center=CENTER, clock_dict=clock60,
                                                                                 clock_hand=minutes),
                                                   length_arrow, NUM_OF_POINTS)

        # Координаты точек на секундной стрелки для отрисовки чисел_стрелок
        points_for_hour_arrow = calculate_points(CENTER, get_position_of_arrow(r=length_arrow,
                                                                               center=CENTER, clock_dict=clock60,
                                                                               clock_hand=hours),
                                                 length_arrow, NUM_OF_POINTS)

        draw_arrow(points_for_hour_arrow, f"{current_time:%H}")  # Отрисовка часовой стрелки
        draw_arrow(points_for_minute_arrow, f"{current_time:%M}")  # Отрисовка минутной стрелки
        draw_arrow(points_for_second_arrow, f"{current_time:%S}")  # Отрисовка секундной стрелки

        pg.draw.circle(surface, pg.Color("#103C13"), CENTER_CIRCLE, 25)  # Отрисовка центральной точки начал стрелок

        time_text_render = font.render(f'{current_time:%H:%M:%S}', True,
                                       pg.Color([randint(0, 254), randint(0, 254),
                                                 randint(0, 254)]))  # Электронные часы

        surface.blit(source=time_text_render, dest=(100, 100))  # Отрисовка электронных часов

        pg.display.flip()
        clock.tick(1)
