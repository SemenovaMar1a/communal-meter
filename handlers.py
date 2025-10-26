from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types.callback_query import CallbackQuery
from aiogram.fsm.context import FSMContext
import kb, text
from states import Electricity, Сold_water, Hot_water, Water_drainage
import utils

router = Router()
global cubes_of_cold_water
global cubes_of_hot_water

"""Начало работы бота"""
@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.greet.format(name=msg.from_user.full_name), reply_markup=kb.menu)

"""Вызов меню"""
@router.message(F.text == "Меню")
@router.message(F.text == "меню")
@router.message(F.text == "Выйти в меню")
async def menu(msg: Message):
    await msg.answer(text.menu, reply_markup=kb.menu)

"""Работа сполучением данных от пользователя и расчетом этих данных"""
"""Электричество"""
@router.callback_query(F.data == "counting_the_communes")
async def counting_the_communes_start(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer("Введи данные по электричеству за прошлый месяц")
    await state.set_state(Electricity.electricity_last_month)

@router.message(F.text, Electricity.electricity_last_month)
async def counting_the_communes_capture_electricity_last_month(msg: Message, state: FSMContext):
    try:
        value = float(msg.text.replace('.','.'))
    except ValueError:
        await msg.answer("Пожалуйста, введи число (например, 123.45)")
        return
    
    await state.update_data(electricity_last_month=value)
    await msg.answer("Теперь напиши данные по электричеству за этот месяц")
    await state.set_state(Electricity.electricity_this_month)

@router.message(F.text, Electricity.electricity_this_month)
async def counting_the_communes_capture_constant_of_electricity(msg: Message, state: FSMContext):
    try:
        value = float(msg.text.replace('.','.'))
    except ValueError:
        await msg.answer("Пожалуйста, введи число (например, 123.45)")
        return
    
    await state.update_data(electricity_this_month=value)
    await msg.answer("Теперь напиши константу по электричеству")
    await state.set_state(Electricity.constant_of_electricity)

@router.message(F.text, Electricity.constant_of_electricity)
async def counting_the_communes_electricity(msg: Message, state: FSMContext):
    try:
        value = float(msg.text.replace('.','.'))
    except ValueError:
        await msg.answer("Пожалуйста, введи число (например, 123.45)")
        return
    
    await state.update_data(constant_of_electricity=value)

    electricity = await state.get_data()

    cubes_of_electricity = electricity.get("electricity_this_month") - electricity.get("electricity_last_month")
    result_electricity = cubes_of_electricity * electricity.get("constant_of_electricity")
    
    await state.update_data(result_electricity=result_electricity)
    await msg.answer(f"Результат по электричеству {result_electricity}р.")
    await msg.answer(text.menu, reply_markup=kb.cold_water)
    
"""Холодная вода"""
@router.callback_query(F.data == "counting_cold_water")
async def counting_the_communes_capture_cold_water_last_month(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer("Теперь напиши данные по холодной воде за прошлый месяц")
    await state.set_state(Сold_water.cold_water_last_month)

@router.message(F.text, Сold_water.cold_water_last_month)
async def counting_the_communes_capture_cold_water_this_month(msg: Message, state: FSMContext):
    try:
        value = float(msg.text.replace('.','.'))
    except ValueError:
        await msg.answer("Пожалуйста, введи число (например, 123.45)")
        return
    
    await state.update_data(cold_water_last_month=value)
    await msg.answer("Теперь напиши данные по холодной воде за этот месяц")
    await state.set_state(Сold_water.cold_water_this_month)

@router.message(F.text, Сold_water.cold_water_this_month)
async def counting_the_communes_capture_constant_of_cold_water(msg: Message, state: FSMContext):
    try:
        value = float(msg.text.replace('.','.'))
    except ValueError:
        await msg.answer("Пожалуйста, введи число (например, 123.45)")
        return
    
    await state.update_data(cold_water_this_month=value)
    await msg.answer("Теперь напиши константу по холодной воде")
    await state.set_state(Сold_water.constant_of_cold_water)

@router.message(F.text, Сold_water.constant_of_cold_water)
async def counting_the_communes_cold_water(msg: Message, state: FSMContext):
    try:
        value = float(msg.text.replace('.','.'))
    except ValueError:
        await msg.answer("Пожалуйста, введи число (например, 123.45)")
        return
    
    await state.update_data(constant_of_cold_water=value)

    сold_water = await state.get_data()
    cubes_of_cold_water = сold_water.get("cold_water_this_month") - сold_water.get("cold_water_last_month")
    result_cold_water = cubes_of_cold_water * сold_water.get("constant_of_cold_water")

    await state.update_data(cubes_of_cold_water=cubes_of_cold_water)
    await state.update_data(result_cold_water=result_cold_water)
    await msg.answer(f"Результат по холодной воде {result_cold_water}р.")
    await msg.answer(text.menu, reply_markup=kb.hot_water)    

"""Горячая вода"""
@router.callback_query(F.data == "counting_hot_water")
async def counting_the_communes_capture_hot_water_last_month(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer("Теперь напиши данные по горячей воде за прошлый месяц")
    await state.set_state(Hot_water.hot_water_last_month)

@router.message(F.text, Hot_water.hot_water_last_month)
async def counting_the_communes_capture_hot_water_this_month(msg: Message, state: FSMContext):
    try:
        value = float(msg.text.replace('.','.'))
    except ValueError:
        await msg.answer("Пожалуйста, введи число (например, 123.45)")
        return
    
    await state.update_data(hot_water_last_month=value)
    await msg.answer("Теперь напиши данные по горячей воде за этот месяц")
    await state.set_state(Hot_water.hot_water_this_month)

@router.message(F.text, Hot_water.hot_water_this_month)
async def counting_the_communes_capture_constant_of_hot_water(msg: Message, state: FSMContext):
    try:
        value = float(msg.text.replace('.','.'))
    except ValueError:
        await msg.answer("Пожалуйста, введи число (например, 123.45)")
        return
    
    await state.update_data(hot_water_this_month=value)
    await msg.answer("Теперь напиши константу по горячей воде")
    await state.set_state(Hot_water.constant_of_hot_water)

@router.message(F.text, Hot_water.constant_of_hot_water)
async def counting_the_communes_hot_water(msg: Message, state: FSMContext):
    try:
        value = float(msg.text.replace('.','.'))
    except ValueError:
        await msg.answer("Пожалуйста, введи число (например, 123.45)")
        return
    
    await state.update_data(constant_of_hot_water=value)

    hot_water = await state.get_data()
    cubes_of_hot_water = hot_water.get("hot_water_this_month") - hot_water.get("hot_water_last_month")
    result_hot_water = cubes_of_hot_water * hot_water.get("constant_of_hot_water")

    await state.update_data(cubes_of_hot_water=cubes_of_hot_water)
    await state.update_data(result_hot_water=result_hot_water)
    await msg.answer(f"Результат по горячей воде {result_hot_water}р.")
    await msg.answer(text.menu, reply_markup=kb.water_drainage)  

@router.callback_query(F.data == "counting_water_drainage")
async def counting_the_communes_capture_water_drainage(clbck: CallbackQuery, state: FSMContext):
    await clbck.message.answer("Теперь напиши данные водоотведения")
    await state.set_state(Water_drainage.water_drainage)

@router.message(F.text, Water_drainage.water_drainage)
async def counting_the_communes_water_drainage(msg: Message, state: FSMContext):
    try:
        value = float(msg.text.replace('.','.'))
    except ValueError:
        await msg.answer("Пожалуйста, введи число (например, 123.45)")
        return
    
    await state.update_data(water_drainage=value)

    data = await state.get_data()
    result_water_drainage = (data.get("cubes_of_hot_water") + data.get("cubes_of_cold_water")) * data.get("water_drainage")

    await state.update_data(result_water_drainage=result_water_drainage)
    await msg.answer(f"Результат по водоотводу {result_water_drainage}р.")
    await msg.answer(text.menu, reply_markup=kb.result)  

@router.callback_query(F.data == "result")
async def counting_the_communes_result(clbck: CallbackQuery, state: FSMContext):
    data = await state.get_data()

    result_water_drainage = data.get("result_electricity") + data.get("result_cold_water") + data.get("result_hot_water") + data.get("result_water_drainage")

    electricity = (f'Электричество: {data.get("electricity_this_month")} - {data.get("electricity_last_month")} = {data.get("electricity_this_month") - data.get("electricity_last_month")} * {data.get("constant_of_electricity")} = {data.get("result_electricity")}')
    cold_water = (f'Холодная вода: {data.get("cold_water_this_month")} - {data.get("cold_water_last_month")} = {data.get("cold_water_this_month") - data.get("cold_water_last_month")} * {data.get("constant_of_cold_water")} = {data.get("result_cold_water")}')
    hot_water = (f'Горячая вода: {data.get("hot_water_this_month")} - {data.get("hot_water_last_month")} = {data.get("hot_water_this_month") - data.get("hot_water_last_month")} * {data.get("constant_of_hot_water")} = {data.get("result_hot_water")}')
    water_drainage = (f'{(data.get("cold_water_this_month") - data.get("cold_water_last_month")) + (int(data.get("hot_water_this_month") - data.get("hot_water_last_month")))} + {data.get('result_water_drainage')} = {data.get('result_water_drainage')}')
    result = (f'Результат: {data.get("result_electricity")} + {data.get("result_cold_water")} + {data.get("result_hot_water")} + {data.get("result_water_drainage")} = {result_water_drainage}')

    if utils.write(electricity, cold_water, hot_water, water_drainage, result):
        await clbck.message.answer("Результаты сохранены")
    else:
        await clbck.message.answer("Произошла ошибка в сохранении данных")

    await clbck.message.answer(f"Результат по комуналке за этот месяц {result_water_drainage}р.")
    state.clear()

@router.callback_query(F.data == "output_of_all_calculations")
async def output_of_all_calculations(clbck: CallbackQuery):
    await clbck.message.answer(utils.read())

