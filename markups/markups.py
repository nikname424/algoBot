from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

#создание кнопки и сессии
mainButton = ReplyKeyboardMarkup(resize_keyboard=True)
pri3v2et2Button = KeyboardButton('Узнать курсы 📚')
pr2iv21et2Button = KeyboardButton('Отправить заявку 📃')

#главная кнопка. 
mainButton.add(pr2iv21et2Button, pri3v2et2Button)

# создание кнопок Inline
mainInlineButtons = InlineKeyboardMarkup()
ExitButtonInline = InlineKeyboardButton('Назад' , callback_data='exit')
KlientButtonInline = InlineKeyboardButton('Записаться' , callback_data='Klient')
mainInlineButtons.add(KlientButtonInline, ExitButtonInline)

# сетка с курсами
coursesMarkup = InlineKeyboardMarkup()
