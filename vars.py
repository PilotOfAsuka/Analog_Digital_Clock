RES = WIDTH, HEIGHT = 800, 800  # Размер окна
font_size = 20  # Размер шрифта

# Центр для стрелок с учетом смещения шрифта
CENTER = H_WIDTH, H_HEIGHT = (WIDTH // 2) - font_size, (HEIGHT // 2) - font_size
CENTER_CIRCLE = [H_WIDTH + font_size, H_HEIGHT + font_size]  # Истинный центр окна

# Словарь разделения окружности на 60 положений и углов к каждому из 60 положений
clock60 = dict(zip(range(60), range(0, 360, 6)))

length_arrow = 260  # Длина стрелки в пикселях
NUM_OF_POINTS = length_arrow // 35  # Количество точек на линии с длиной length_arrow и шагом 35 пикселей
