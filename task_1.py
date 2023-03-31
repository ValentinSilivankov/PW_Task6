geo_logs = [
    {"visit1": ["Москва", "Россия"]},
    {"visit2": ["Дели", "Индия"]},
    {"visit3": ["Владимир", "Россия"]},
    {"visit4": ["Лиссабон", "Португалия"]},
    {"visit5": ["Париж", "Франция"]},
    {"visit6": ["Лиссабон", "Португалия"]},
    {"visit7": ["Тула", "Россия"]},
    {"visit8": ["Тула", "Россия"]},
    {"visit9": ["Курск", "Россия"]},
    {"visit10": ["Архангельск", "Россия"]},
]

geo_logs_true = [
    {"visit1": ["Москва", "Россия"]},
    {"visit3": ["Владимир", "Россия"]},
    {"visit7": ["Тула", "Россия"]},
    {"visit8": ["Тула", "Россия"]},
    {"visit9": ["Курск", "Россия"]},
    {"visit10": ["Архангельск", "Россия"]},
]


def geo_logs_rus(geo_logs):
    geo_logs_rus = []
    for visits in geo_logs:
        for country in visits.values():
            if country[1] == "Россия":
                geo_logs_rus.append(visits)
    return geo_logs_rus