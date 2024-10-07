import asyncio
from telebot.async_telebot import AsyncTeleBot
from config import token
from send import send_application 
from db import Database
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bot = AsyncTeleBot(token)

db = Database('Database.db')
mainButton = ReplyKeyboardMarkup(resize_keyboard=True)
pri3v2et2Button = KeyboardButton('Узнать курсы 📚')
pr2iv21et2Button = KeyboardButton('Отправить заявку 📃')
mainButton.add(pr2iv21et2Button, pri3v2et2Button)
steps = {}

@bot.message_handler(commands=['start'])
async def start(message):
    global steps
    if db.is_register(message.from_user.id):
        db.register_user(message.from_user.id)
    await bot.send_message(message.from_user.id, text='Привет\nМеня зовут Алгобот.\nЯ помогу подобрать нужный курс для Вашего ребёнка 😊 \nНажмите "Отправить заявку 📃" для заполнения кратенькой анкеты. Ваша заявка моментально поступит нашему менеджеру 👩\nДля ознакомления с нашими курсами нажмите "Узнать курсы 📚"', reply_markup=mainButton)
    steps[message.from_user.id] = 1
    if message.from_user.id == 'Отправить заявку 📃':
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
            elif message.from_user.id == 'Узнать курсы 📚':
                # задача никиты
                print('ggg')
@bot.callback_query_handler(func=lambda call: True)
async def get_callback(call): 
    if call.data == 'test': 
        print('hello')

async def main():
    await bot.infinity_polling()

if __name__ == "__main__":
    asyncio.run(main())
    
