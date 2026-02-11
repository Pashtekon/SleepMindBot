from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

age = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='10-14 лет', callback_data='age_10-14'), InlineKeyboardButton(text='15-16 лет', callback_data='age_15-16')],
    [InlineKeyboardButton(text='17-18 лет', callback_data='age_17-18'), InlineKeyboardButton(text='Старше 18 лет', callback_data='age_18<')]
])


gender = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Мужской', callback_data='gender_Мужской'), InlineKeyboardButton(text='Женский', callback_data='gender_Женский')],
])


health_rate = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Отличное', callback_data='rate_Отличное'), InlineKeyboardButton(text='Хорошее', callback_data='rate_Хорошее')],
    [InlineKeyboardButton(text='Среднее', callback_data='rate_Среднее'), InlineKeyboardButton(text='Плохое', callback_data='rate_Плохое')]
])


hours_sleep = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Менее 6 часов', callback_data='hours_6>'), InlineKeyboardButton(text='6-7 часов', callback_data='hours_6-7')],
    [InlineKeyboardButton(text='7-8 часов', callback_data='hours_7-8'), InlineKeyboardButton(text='Более 8 часов', callback_data='hours_8<')]
])


hard_to_sleep = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Да, почти каждый вечер', callback_data='hard_Да, почти каждый вечер'), InlineKeyboardButton(text='Иногда', callback_data='hard_Иногда')],
    [InlineKeyboardButton(text='Редко', callback_data='hard_Редко'), InlineKeyboardButton(text='Никогда', callback_data='hard_Никогда')]
])


often_wakeup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Регулярно', callback_data='wakeup_Регулярно'), InlineKeyboardButton(text='Время от времени', callback_data='wakeup_Время от времени')],
    [InlineKeyboardButton(text='Очень редко', callback_data='wakeup_Очень редко'), InlineKeyboardButton(text='Практически никогда', callback_data='wakeup_Практически никогда')]
])

time_sleep_map = {
    "und22": "До 22:00",
    "22-23": "От 22:00 до 23:00",
    "23-00": "От 23:00 до полуночи",
    "aft00": "Позже полуночи"
}

time_sleep = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='До 22:00', callback_data='time_und22'), InlineKeyboardButton(text='От 22:00 до 23:00', callback_data='time_22-23')],
    [InlineKeyboardButton(text='От 23:00 до полуночи', callback_data='time_23-00'), InlineKeyboardButton(text='Позже полуночи', callback_data='time_aft00')]
])

trouble_to_sleep_map = {
    "dev": "Электронные устройства(телефон, компьютер)",
    "thnk": "Мысли и переживания",
    "noise": "Громкая музыка или шум вокруг",
    "act": "Физическая активность перед сном",
    "other": "Другое"
}


trouble_to_sleep = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Электронные устройства(телефон, компьютер)', callback_data='trouble_dev')], 
    [InlineKeyboardButton(text='Мысли и переживания', callback_data='trouble_thnk')],
    [InlineKeyboardButton(text='Громкая музыка или шум вокруг', callback_data='trouble_noise')], 
    [InlineKeyboardButton(text='Физическая активность перед сном', callback_data='trouble_act')],
    [InlineKeyboardButton(text='Другое', callback_data='trouble_other')]
])


tired_morning = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Всегда', callback_data='tired_Всегда'), InlineKeyboardButton(text='Часто', callback_data='tired_Часто')],
    [InlineKeyboardButton(text='Изредка', callback_data='tired_Изредка'), InlineKeyboardButton(text='Почти никогда', callback_data='tired_Почти никогда')]
])


bad_mood_map = {
    "alw": "Постоянно замечаю",
    "usl": "Обычно такое бывает",
    "rare": "Редко испытываю такие проблемы",
    "no": "Нет, настроение не зависит от сна"
}


bad_mood = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Постоянно замечаю', callback_data='mood_alw'), InlineKeyboardButton(text='Обычно такое бывает', callback_data='mood_usl')],
    [InlineKeyboardButton(text='Редко испытываю такие проблемы', callback_data='mood_rare')],
    [InlineKeyboardButton(text='Нет, настроение не зависит от сна', callback_data='mood_no')]
])


angry_mood_map = {
    "ofn": "Очень часто",
    "per": "Периодически",
    "rare": "Крайне редко",
    "no": "Не испытываю такого состояния"
}


angry_mood = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Очень часто', callback_data='angry_ofn'), InlineKeyboardButton(text='Периодически', callback_data='angry_per')],
    [InlineKeyboardButton(text='Крайне редко', callback_data='angry_rare'), InlineKeyboardButton(text='Не испытываю такого состояния', callback_data='angry_no')]
])


easier_tasks = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Определенно легче', callback_data='easier_Определенно легче'), InlineKeyboardButton(text='Немного проще', callback_data='easier_Немного проще')],
    [InlineKeyboardButton(text='Без разницы', callback_data='easier_Без разницы'), InlineKeyboardButton(text='Хуже справляюсь', callback_data='easier_Хуже справляюсь')]
])


headaches = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Частые случаи', callback_data='headaches_Частые случаи'), InlineKeyboardButton(text='Случается иногда', callback_data='headaches_Случается иногда')],
    [InlineKeyboardButton(text='Бывает крайне редко', callback_data='headaches_Бывает крайне редко'), InlineKeyboardButton(text='Никогда не сталкивался', callback_data='headaches_Никогда не сталкивался')]
])


anxiety = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Значительно повышается', callback_data='anxiety_Значительно повышается')], 
    [InlineKeyboardButton(text='Незначительное повышение', callback_data='anxiety_Незначительное повышение')],
    [InlineKeyboardButton(text='Остаюсь спокойным(-ой)', callback_data='anxiety_Остаюсь спокойным(-ой)')], 
    [InlineKeyboardButton(text='Уровень тревоги снижается', callback_data='anxiety_Уровень тревоги снижается')]
])


less_concentration_map = {
    "very": "Это сильно влияет на мою память и внимание",
    "lit": "Небольшое влияние присутствует",
    "no": "Практически не влияет",
    "bett": "Улучшение когнитивных функций наблюдается"
}


less_concentration = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Это сильно влияет на мою память и внимание', callback_data='less_very')], 
    [InlineKeyboardButton(text='Небольшое влияние присутствует', callback_data='less_lit')],
    [InlineKeyboardButton(text='Практически не влияет', callback_data='less_no')], 
    [InlineKeyboardButton(text='Улучшение когнитивных функций наблюдается', callback_data='less_bett')]
])


trouble_education = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Проблемы значительные', callback_data='education_Проблемы значительные')], 
    [InlineKeyboardButton(text='Есть небольшие сложности', callback_data='education_Есть небольшие сложности')],
    [InlineKeyboardButton(text='Едва ощутимые последствия', callback_data='education_Едва ощутимые последствия')], 
    [InlineKeyboardButton(text='Никаких проблем не возникает', callback_data='education_Никаких проблем не возникает')]
])


miss_lessons = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Регулярно', callback_data='miss_Регулярно'), InlineKeyboardButton(text='Несколько раз было', callback_data='miss_Несколько раз было')],
    [InlineKeyboardButton(text='Только однажды', callback_data='miss_Только однажды'), InlineKeyboardButton(text='Никогда не случалось', callback_data='miss_Никогда не случалось')]
])


satisfied_map = {
    "allno": "Совершенно неудовлетворен(-на)",
    "maybno": "Скорее неудовлетворен(-на)",
    "midy": "Средне удовлетворен(-на)",
    "mayby": "Довольно удовлетворен(-на)",
    "ally": "Абсолютно удовлетворен(-на)"
}


satisfied = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Совершенно неудовлетворен(-на)', callback_data='satisfied_allno'), InlineKeyboardButton(text='Скорее неудовлетворен(-на)', callback_data='satisfied_maybno')],
    [InlineKeyboardButton(text='Средне удовлетворен(-на)', callback_data='satisfied_midy'), InlineKeyboardButton(text='Довольно удовлетворен(-на)', callback_data='satisfied_mayby')],
    [InlineKeyboardButton(text='Абсолютно удовлетворен(-на)', callback_data='satisfied_ally')]
])


often_dreams = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Регулярно(каждую ночь)', callback_data='dreams_Регулярно(каждую ночь)'), InlineKeyboardButton(text='Случается иногда', callback_data='dreams_Случается иногда')],
    [InlineKeyboardButton(text='Бывает крайне редко', callback_data='dreams_Бывает крайне редко'), InlineKeyboardButton(text='Никогда не снятся', callback_data='dreams_Никогда не снятся')]
])


color_dreams = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Черно-белые', callback_data='color_Черно-белые'), InlineKeyboardButton(text='Цветные', callback_data='color_Цветные')],
    [InlineKeyboardButton(text='Не обращаю внимание на цвет сна', callback_data='color_Не обращаю внимание на цвет сна')]
])