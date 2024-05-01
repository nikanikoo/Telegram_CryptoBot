import telebot
import json
from telebot import types

TOKEN = "token"

bot = telebot.TeleBot(token=TOKEN, parse_mode="Markdown")

@bot.message_handler(commands=["start"])
def start(message):
    id = message.from_user.id
    create_user(id)

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="👛 Кошелёк", callback_data='wallet')
    btn2 = types.InlineKeyboardButton(text="🍑 Подписки", callback_data='subscriptions')
    btn3 = types.InlineKeyboardButton(text="💠 P2P", callback_data="p2p")
    btn4 = types.InlineKeyboardButton(text="🐋 Биржа", callback_data="exchage")
    btn5 = types.InlineKeyboardButton(text="🦋 Чеки", callback_data='checks')
    btn6 = types.InlineKeyboardButton(text="📥 Счета", callback_data='checkouts')
    btn7 = types.InlineKeyboardButton(text="🏝️ Crypto Pay", callback_data='crypto_pay')
    btn8 = types.InlineKeyboardButton(text='🎁 Розыгрыши', callback_data="prizes")
    btn9 = types.InlineKeyboardButton(text="🎖️ Конкурсы", callback_data="contests")
    btn10 = types.InlineKeyboardButton(text="⚙️ Настройки", callback_data="settings")

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, row_width=2)

    bot.send_message(chat_id=message.chat.id, text="👛 *Мультивалютный криптокошелёк*. Покупайте, продавайте, храните, *отправляйте* и платите криптовалютой, когда хотите.\n\nПодписывайтесь на [наш канал](https://dsc.gg/firefrogstudios) и вступайте в [наш чат](https://dsc.gg/firefrogstudios).", reply_markup=markup)

@bot.message_handler(commands=["wallet"])
def wallet(message):
    id = message.from_user.id
    create_user(id)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Пополнить", callback_data="deposit")
    btn2 = types.InlineKeyboardButton(text="Вывести", callback_data="get")
    btn3 = types.InlineKeyboardButton(text="Адресная книга", callback_data="adress_book")
    btn4 = types.InlineKeyboardButton(text="Скрыть мелкие балансы", callback_data="hide_small_balance")
    btn5 = types.InlineKeyboardButton(text="Комиссии и лимиты", callback_data="limits")
    btn6 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="back_wallet")
    markup.add(btn1, btn2, row_width=2)
    markup.add(btn3, btn4, btn5, btn6, row_width=1)
    bot.send_message(chat_id=message.chat.id, text=f"👛 *Кошелёк*\n\n*Tether*: {balance(id, 'USDT')} USDT\n\n*Toncoin*: {balance(id, 'TON')} TON\n\n*Gram*: {balance(id, 'GRAM')} GRAM\n\n*Bitcoin*: {balance(id, 'BTC')} BTC\n\n*Litecoin*: {balance(id, 'LTC')} LTC\n\n*Ethereum*: {balance(id, 'ETH')} ETH\n\n*Binance Coin*: {balance(id, 'BNB')} BNB\n\n*TRON*: {balance(id, 'TRX')} TRX\n\n*USD Coin*: {balance(id, 'USDC')} USDC", reply_markup=markup)

@bot.message_handler(commands=["add_amount"])
def add_amount(message):
    id = str(message.from_user.id)
    data_user = load_user_data()
    if data_user[id]["is_admin"] == True:
        args = message.text.split()[1:]
        if len(args) != 3:
            bot.send_message(chat_id=message.chat.id, text="Неверное количество аргументов.")
            return
        id_recipied = str(args[0])
        account = args[1]
        amount = float(args[2])
        markup = types.InlineKeyboardMarkup()
        btn = types.InlineKeyboardButton(text="👛 Открыть кошелёк", callback_data="wallet")
        markup.add(btn)
        change_balance(id, account, amount)
        bot.reply_to(message=message, text=f"Баланс успешно изменен. Новый баланс {account}: {amount} для пользователя с id {id_recipied}")
        bot.send_message(chat_id=id_recipied, text=f"👛 Успешное пополнение. Вы получили {amount} {account}.", reply_markup=markup)

@bot.message_handler(commands=["set_admin"])
def set_admin(message):
    id = str(message.from_user.id)
    data_user = load_user_data()
    if data_user[id]["is_admin"] == 1:
        args = message.text.split()[1:]
        if len(args) != 1:
            bot.send_message(chat_id=message.chat.id, text="Неверное количество аргументов.")
            return
        id_setadmin = str(args[0])
        data_user[id_setadmin]['is_admin'] = 1
        save_user_data(data_user)
        bot.send_message(chat_id=message.chat.id, text=f"Пользователь с id {id_setadmin} успешно стал администратором!")

@bot.message_handler(commands=["rem_admin"])
def rem_admin(message):
    id = str(message.from_user.id)
    data_user = load_user_data()
    if data_user[id]["is_admin"] == 1:
        args = message.text.split()[1:]
        if len(args) != 1:
            bot.send_message(chat_id=message.chat.id, text="Неверное количество аргументов.")
            return
        id_setadmin = str(args[0])
        data_user[id_setadmin]['is_admin'] = 0
        save_user_data(data_user)
        bot.send_message(chat_id=message.chat.id, text=f"Пользователь с id {id_setadmin} был отозван!")

@bot.callback_query_handler(func=lambda call: call.data == "back_wallet")
def back_wallet(call):
    id = call.from_user.id
    create_user(id)

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="👛 Кошелёк", callback_data='wallet')
    btn2 = types.InlineKeyboardButton(text="🍑 Подписки", callback_data='subscriptions')
    btn3 = types.InlineKeyboardButton(text="💠 P2P", callback_data="p2p")
    btn4 = types.InlineKeyboardButton(text="🐋 Биржа", callback_data="exchage")
    btn5 = types.InlineKeyboardButton(text="🦋 Чеки", callback_data='checks')
    btn6 = types.InlineKeyboardButton(text="📥 Счета", callback_data='checkouts')
    btn7 = types.InlineKeyboardButton(text="🏝️ Crypto Pay", callback_data='crypto_pay')
    btn8 = types.InlineKeyboardButton(text='🎁 Розыгрыши', callback_data="prizes")
    btn9 = types.InlineKeyboardButton(text="🎖️ Конкурсы", callback_data="contests")
    btn10 = types.InlineKeyboardButton(text="⚙️ Настройки", callback_data="settings")

    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, row_width=2)

    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="👛 *Мультивалютный криптокошелёк*. Покупайте, продавайте, храните, *отправляйте* и платите криптовалютой, когда хотите.\n\nПодписывайтесь на [наш канал](https://dsc.gg/firefrogstudios) и вступайте в [наш чат](https://dsc.gg/firefrogstudios).", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "wallet")
def wallet_btn(call):
    id = call.from_user.id
    create_user(id)
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Пополнить", callback_data="deposit")
    btn2 = types.InlineKeyboardButton(text="Вывести", callback_data="get")
    btn3 = types.InlineKeyboardButton(text="Адресная книга", callback_data="adress_book")
    btn4 = types.InlineKeyboardButton(text="Скрыть мелкие балансы", callback_data="hide_small_balance")
    btn5 = types.InlineKeyboardButton(text="Комиссии и лимиты", callback_data="limits")
    btn6 = types.InlineKeyboardButton(text="🔙 Назад", callback_data="back_wallet")
    markup.add(btn1, btn2, row_width=2)
    markup.add(btn3, btn4, btn5, btn6, row_width=1)
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=f"👛 *Кошелёк*\n\n*Tether*: {balance(id, 'USDT')} USDT\n\n*Toncoin*: {balance(id, 'TON')} TON\n\n*Gram*: {balance(id, 'GRAM')} GRAM\n\n*Bitcoin*: {balance(id, 'BTC')} BTC\n\n*Litecoin*: {balance(id, 'LTC')} LTC\n\n*Ethereum*: {balance(id, 'ETH')} ETH\n\n*Binance Coin*: {balance(id, 'BNB')} BNB\n\n*TRON*: {balance(id, 'TRX')} TRX\n\n*USD Coin*: {balance(id, 'USDC')} USDC", reply_markup=markup)

# Utils

def save_user_data(user_data):
    with open('stats.json', 'w') as file:
        json.dump(user_data, file)

def load_user_data():
    with open('stats.json', 'r') as file:
        user_data = json.load(file)
    return user_data

def create_user(id):
    user_data = load_user_data()
    id = str(id)
    if id not in user_data:
        user_data[id] = {
            'USDT': 0,
            'TON': 0,
            'GRAM': 0,
            'BTC': 0,
            'LTC': 0,
            'ETH': 0,
            'BNB': 0,
            'TRX': 0,
            'USDC': 0,
            'is_admin': False
            }
        save_user_data(user_data)
    else:
        return

def balance(user_id, account):
    user_id = str(user_id)
    user_data = load_user_data()
    balance = user_data[user_id][account]
    return balance

def change_balance(id, account, amount):
    id = str(id)
    user_data = load_user_data()
    user_data[id][str(account)] += amount
    save_user_data(user_data)

bot.infinity_polling()