from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_data import course_callback, book_callback
categoryMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💻 Kurslar", callback_data="courses"),
            InlineKeyboardButton(text="📚 Kitoblar", callback_data="books"),
        ],
        [
            InlineKeyboardButton(text="👓 Mohirdev sahifasiga o'tish", url="https://old.mohirdev.uz/courses/telegram/"),
        ],
        [
            InlineKeyboardButton(text="🔍 Qidirish", switch_inline_query_current_chat=""),
        ],
        [
            InlineKeyboardButton(text="✉️ Ulashish", switch_inline_query="Zo'r bot ekan"),
        ],
    ])

coursesMenu = InlineKeyboardMarkup(row_width=1)


python = InlineKeyboardButton(text="🐍 Python Dasturlash Asoslari", callback_data=course_callback.new(item_name="python"))
coursesMenu.insert(python)

django = InlineKeyboardButton(text="🌍 Django Web Dasturlash", callback_data=course_callback.new(item_name="django"))
coursesMenu.insert(django)

telegram = InlineKeyboardButton(text="🤖 Mukammal Telegram bot", callback_data="course:telegram")
coursesMenu.insert(telegram)

algorithm = InlineKeyboardButton(text="📈 Malumotlar Tuzulmasi va Algoritmlar", callback_data="course: algorithm")
coursesMenu.insert(algorithm)

back_button = InlineKeyboardButton(text="🔙 Ortga", callback_data="cancel")
coursesMenu.insert(back_button)

books = {
    "Python. Dasturlash asoslari": "python_book",
    "C++. Dasturlash tili": "cpp_book",
    "Mukammal Dasturlash, JavaScript": "js_book",
}

booksMenu = InlineKeyboardMarkup(row_width=1)
for key, value in books.items():
    booksMenu.insert(InlineKeyboardButton(text=key, callback_data=book_callback.new(item_name=value)))
booksMenu.insert(back_button)

telegram_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Xarid qilish", url="https://old.mohirdev.uz/courses/telegram")
    ]
])

algoritm_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    InlineKeyboardButton(text="Ko'rish", url="https://old.mohirdev.uz/courses/algoritmlar/")
])