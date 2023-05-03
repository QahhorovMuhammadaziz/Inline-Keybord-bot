from aiogram import types


from loader import dp
from aiogram.utils.markdown import hbold, hcode, hitalic, hunderline, hstrikethrough, hlink


@dp.message_handler(commands='info_html')
async def bot_info(message: types.Message):
    text = f"Assalomu alaykum, {message.from_user.full_name}!\n"
    text += "Bu <b>qalin yozuv.</b>\n"
    text += "Bu esa<i>egri matn.</i>\n"
    text += "Bu <u>ostiga chizilgan matn.</u>\n"
    text += "Bu esa <s>ochirilgan matn.</s>\n"
    text += "Bu esa <a href='https://mohirdev.uz' >Mohirdev sahifasiga link</a>.\n"
    text += "Bu esa <code>print('Hello World')</code>kod.\n"
    
    
    await message.answer(text)


@dp.message_handler(commands='info_markdown')
async def bot_info(message: types.Message):
    text = f"Assalomu alaykum, {message.from_user.full_name}\!\n"
    text += "Bu *qalin yozuv*\n"
    text += "Bu esa _egri matn_\n"
    text += "Bu __ostki chizilgan matn__\n"
    text += "Bu esa ~o'chirilgan matn~"
    text += "Bu esa [Mohirdev sahifasiga link](https://mohirdev.uz)\n"
    text += "Bu esa `print('Hello World')`"
    
    await message.answer(text, parse_mode=types.ParseMode.MARKDOWN_V2)



@dp.message_handler(commands='info')
async def bot_info(message: types.Message):
    text = f"Assalomu alaykum, {message.from_user.full_name}!\n"
    text += "Bu" + hbold('qalin yozuv.\n')
    text += "Bu esa" + hitalic('egri matn.\n')
    text += "Bu" + hunderline('ostiga chizilgan matn.\n')
    text += "Bu esa" + hstrikethrough('ochirilgan matn.\n')
    text += "Bu esa" + hlink('Mohirdev sahifasiga link\n', 'https://mohirdev.uz')
    text += "Bu esa" + hcode ('print("Hello World!")') + "kod\n"
    await message.answer(text)