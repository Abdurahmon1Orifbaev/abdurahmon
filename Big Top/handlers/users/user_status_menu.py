from aiogram import types

from keyboards.default.user_status_menu import user_order_menu
from loader import dp, db_manager


@dp.message_handler(text="🛒 Buyurtmalar")
async def user_order_menu_handler(message: types.Message):
    text = "Quyidagi tugmachalardan birini tanlang."
    await message.answer(text=text, reply_markup=user_order_menu)


@dp.message_handler(text="⏳ Kutilayotganlar")
async def user_order_waiting_handler(message: types.Message):
    orders = db_manager.get_all_orders_by_status(message.chat.id, "Kutilmoqda")
    if len(orders) == 0:
        text = "Hozirda kutilayotgan buyurtmalar mavjud emas."
        await message.answer(text=text)
    else:
        for order in orders:
            order_items = db_manager.get_order_items_by_order_id(order[2])
            products = ""
            counter = 1
            total_price = 0
            for item in order_items:
                total_price += float(item[4]) * float(item[3])
                products += f"{counter})\t {item[2]}\t| {item[4]} ta\t| {item[3]} so'm\n"
                counter += 1
            text = f"""
🆔 {order[2]}
⏳ {order[3]}
⏰ {order[4]}

{products}
Jami: {total_price} so'm
"""
            await message.answer(text=text)


@dp.message_handler(text="✅ Qabul qilinganlar")
async def user_order_waiting_handler(message: types.Message):
    orders = db_manager.get_all_orders_by_status(message.chat.id, "Qabul qilingan")
    if len(orders) == 0:
        text = "Hozirda Qabul qilingan buyurtmalar mavjud emas."
        await message.answer(text=text)
    else:
        for order in orders:
            order_items = db_manager.get_order_items_by_order_id(order[2])
            products = ""
            counter = 1
            total_price = 0
            for item in order_items:
                total_price += float(item[4]) * float(item[3])
                products += f"{counter})\t {item[2]}\t| {item[4]} ta\t| {item[3]} so'm\n"
                counter += 1
            text = f"""
🆔 {order[2]}
⏳ {order[3]}
⏰ {order[4]}

{products}
Jami: {total_price} so'm
"""
            await message.answer(text=text)


@dp.message_handler(text="❌ Bekor qilinganlar")
async def user_order_waiting_handler(message: types.Message):
    orders = db_manager.get_all_orders_by_status(message.chat.id, "Bekor qilingan")
    if len(orders) == 0:
        text = "Bekor qilingan buyurtmalar mavjud emas."
        await message.answer(text=text)
    else:
        for order in orders:
            order_items = db_manager.get_order_items_by_order_id(order[2])
            products = ""
            counter = 1
            total_price = 0
            for item in order_items:
                total_price += float(item[4]) * float(item[3])
                products += f"{counter})\t {item[2]}\t| {item[4]} ta\t| {item[3]} so'm\n"
                counter += 1
            text = f"""
🆔 {order[2]}
⏳ {order[3]}
⏰ {order[4]}

{products}
Jami: {total_price} so'm
    """
            await message.answer(text=text)
