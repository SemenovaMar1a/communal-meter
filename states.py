from aiogram.fsm.state import StatesGroup, State

class Electricity(StatesGroup):
    electricity_this_month = State()
    electricity_last_month = State()
    constant_of_electricity = State()
    result_electricity = State()

class Сold_water(StatesGroup):
    cold_water_this_month = State()
    cold_water_last_month = State()
    constant_of_cold_water = State()
    cubes_of_cold_water = State()
    result_cold_water = State()

class Hot_water(StatesGroup):
    hot_water_this_month = State()
    hot_water_last_month = State()
    constant_of_hot_water = State()
    cubes_of_hot_water = State()
    result_hot_water = State()

class Water_drainage(StatesGroup):
    water_drainage = State()
    result_water_drainage = State()