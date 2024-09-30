import asyncio
from telebot.async_telebot import AsyncTeleBot
from config import token
from send import send_application 
from db import Database

bot = AsyncTeleBot(token)

db = Database('Database.db')

steps = {}

@bot.message_handler(commands=['start'])
async def start(message):
    global steps
    if db.is_register(message.from_user.id):
        db.register_user(message.from_user.id)
    
    test_button = Inline
    await bot.send_message(message.from_user.id, text=f'Привет {message.from_user.username}')
    await bot.send_message(message.from_user.id, text='Как зовут вашего ребенка?')
    steps[message.from_user.id] = 1

@bot.message_handler()
async def sss(message):
    global steps, years, name, number
    print(steps)

    if steps[message.from_user.id] == 1: #сюда придёт имя ребёнка
        name = message.text
        db.add_name(message.from_user.id, name)
        await bot.send_message(message.from_user.id, text=f'Хорошее имя {name}')
        await bot.send_message(message.from_user.id, text='Сколько лет вашему ребенку?')
        steps[message.from_user.id] = 2
        
    elif steps[message.from_user.id] == 2: #сюда придёт возраст ребёнка
        years = message.text
        db.add_old(message.from_user.id , years)
        await bot.send_message(message.from_user.id, text=f'Вашего ребенка зовут {name} и ему  {years} лет')
        steps[message.from_user.id] = 4
        await bot.send_message(message.from_user.id, text='Укажите контакт (номер телефона)')

    elif steps[message.from_user.id] == 4: 
        number = message.text
        db.add_phone(message.from_user.id, number)
        await bot.send_message(message.from_user.id, text=f'Заявка была отправлена нашему менеджеру')
        message = f'Новая заявка!\nИмя - {name} \nВозраст - {years} \nИнтересующий курс -   \nНомер родителя  -  {number}  \nЗапись на курс - \nПОРА РАБОТАТЬ!  '
        send_application(user_id=5221339225, token=token, message=message)

@bot.callback_query_handler(func=lambda call: True)
async def get_callback(call): 
    if call.data == 'test': 
        print('hello')

async def main():
    await bot.infinity_polling()

if __name__ == "__main__":
    asyncio.run(main())
    
