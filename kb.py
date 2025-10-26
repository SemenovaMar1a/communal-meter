from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu = [
    [InlineKeyboardButton(text="Подсчет коммуналки", callback_data='counting_the_communes')],
    [InlineKeyboardButton(text="Вывод данных подсчетов", callback_data='output_of_calculation_data')],
    [InlineKeyboardButton(text="Вывод всех записей", callback_data='output_of_all_calculations')]
]

menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='◀️ Выйти в меню')]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="◀️ Выйти в меню", callback_data='menu')]])

cold_water_button = InlineKeyboardButton(text="Подсчет холодной воды", callback_data='counting_cold_water')
cold_water = InlineKeyboardMarkup(inline_keyboard=[[cold_water_button]])

hot_water_button = InlineKeyboardButton(text="Подсчет горячей воды", callback_data='counting_hot_water')
hot_water = InlineKeyboardMarkup(inline_keyboard=[[hot_water_button]])

water_drainage_button = InlineKeyboardButton(text="Подсчет водоотвода", callback_data='counting_water_drainage')
water_drainage = InlineKeyboardMarkup(inline_keyboard=[[water_drainage_button]])

result_button = InlineKeyboardButton(text="Результат", callback_data='result')
result = InlineKeyboardMarkup(inline_keyboard=[[result_button]])