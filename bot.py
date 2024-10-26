from telebot.async_telebot import AsyncTeleBot
from config import token
from send import send_application 
from funcs.db import Database
from markups.markups import mainButton, coursesMarkup
from telebot.types import InlineKeyboardButton
import asyncio
from time import *

bot = AsyncTeleBot(token)

db = Database('Database.db')
steps = {}

@bot.message_handler(commands=['start'])
async def start(message):
    global steps
    if db.is_register(message.from_user.id):
        db.register_user(message.from_user.id)
    await bot.send_message(message.from_user.id, text='Привет\nМеня зовут Алгобот.\nЯ помогу подобрать нужный курс для Вашего ребёнка 😊 \nНажмите "Отправить заявку 📃" для заполнения кратенькой анкеты. Ваша заявка моментально поступит нашему менеджеру 👩\nДля ознакомления с нашими курсами нажмите "Узнать курсы 📚"', reply_markup=mainButton)

@bot.message_handler()
async def sss(message):
    if message.text == 'Отправить заявку 📃':
        # тут отправляем сообщению. 
        await bot.send_message(message.from_user.id, text='Начнем заполнение анкеты?')
        steps[message.from_user.id] = 1

    if message.text == 'Узнать курсы 📚':
        list_course = db.showCourse()
        num = 0
        for course in list_course:
            coursesMarkup.add(InlineKeyboardButton(course, callback_data=f'{course}'))
            num += 1

        await bot.send_message(message.from_user.id, text='Сколько лет вашему ребенку?', reply_markup=coursesMarkup)

    elif steps[message.from_user.id] == 1: #сюда придёт имя ребёнка
        name = message.text
        db.add_name(message.from_user.id, name)

        await bot.send_message(message.from_user.id, text='Сколько лет вашему ребенку?')
        steps[message.from_user.id] = 2
        
    elif steps[message.from_user.id] == 2: #сюда придёт возраст ребёнка
        years = message.text
        db.add_old(message.from_user.id , years)

        steps[message.from_user.id] = 3
        await bot.send_message(message.from_user.id, text='Укажите контакт (номер телефона)')

    elif steps[message.from_user.id] == 4: 
        number = message.text
        db.add_phone(message.from_user.id, number)
        await bot.send_message(message.from_user.id, text=f'Заявка была отправлена нашему менеджеру')
        message = f'Новая заявка!\nИмя - {name} \nВозраст - {years} \nИнтересующий курс -   \nНомер родителя  -  {number}  \nЗапись на курс - \nПОРА РАБОТАТЬ!  '
        send_application(user_id=5221339225, token=token, message=message)

@bot.callback_query_handler(func=lambda call: True)
async def get_callback(call): 
    list_courses = db.showCourse()

    if call.data in list_courses:
        info = db.showInfoCourse(call.data)
        print(info) 

async def main():
    await bot.infinity_polling()

if __name__ == "__main__":
    asyncio.run(main())
    
