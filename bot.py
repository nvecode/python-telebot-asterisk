import telebot
from telebot import types
import subprocess
import logging
import datetime

# Bot token
bot_token = ''
bot = telebot.TeleBot(bot_token)

# Users
trusted_users = {
    'Администратор': ''
}

# Create files
logging.basicConfig(filename='event_bot.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Start
@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id not in trusted_users.values():
        bot.reply_to(message, "У вас нет разрешения на выполнение команд!")
    else:
        global keyboard
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Выключить правило')
        btn2 = types.KeyboardButton('Включить правило')
        keyboard.add(btn1, btn2)

        bot.send_message(message.chat.id, "Выберите действие:", reply_markup=keyboard)
        bot.register_next_step_handler(message, on_click)

def sendMessageAdmin(idUser, commandName):
    for name, value in trusted_users.items():
        if value == idUser and idUser != 460221344:
            bot.send_message(460221344, f'Пользователь - "{name}" - выполнил(а) команду - "{commandName}"')

# Treatment button
@bot.message_handler(func=lambda message: True)
def on_click(message):
    user_id = message.from_user.id
    button_pressed = message.text
    logging.info(f'User {user_id} pressed the button: {button_pressed}')

    if message.text == 'Выключить правило':
        command = '/home/master/telebot-python/python-bot-callcenter/disable.sh'
        subprocess.run(command, shell=True, text=True, timeout=60)
        bot.send_message(message.chat.id, f'Правило успешно выключёно!')
        sendMessageAdmin(user_id, message.text)
        bot.send_message(message.chat.id, "Выберите команду:", reply_markup=keyboard)

    elif message.text == 'Включить правило':
        command = '/home/master/telebot-python/python-bot-callcenter/enable.sh'
        subprocess.run(command, shell=True, text=True, timeout=60)
        bot.send_message(message.chat.id, f'Правило успешно включёно!')
        sendMessageAdmin(user_id, message.text)
        bot.send_message(message.chat.id, "Выберите команду:", reply_markup=keyboard)

# Start bot
bot.polling(none_stop=True)