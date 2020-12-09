import telebot
from config import TOKEN
import keyboard
from data import get_data

bot = telebot.TeleBot(TOKEN)
currency = get_data()

@bot.message_handler(commands=['start'])
def hello(message):
    print(message)
    bot.send_message(
        chat_id=message.chat.id,
        text='Привіт ' + message.chat.first_name,
        reply_markup=keyboard.mainKeyboard()
    )


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(
        chat_id=message.chat.id,
        text='Цей бот призначений для навчання'
             'Для додаткової інформації звертайтесь до творця бота',
        reply_markup=keyboard.mainKeyboard()
    )


@bot.message_handler(content_types=['text'])
def keyboard_func(message):
    text = message.text.lower()

    if text == 'курси валют':
        bot.send_message(
            chat_id=message.chat.id,
            text='Курси валют',
            reply_markup=keyboard.rate_menu()
        )
    elif text == 'обмін валют':
        bot.send_message(
            chat_id=message.chat.id,
            text='Оберіть валюту яку хочете обміняти',
            reply_markup=keyboard.exchange_menu(),
        )
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text="Немає такої команди",
            reply_markup=keyboard.mainKeyboard()
        )

@bot.callback_query_handler(func=lambda call: call.data == 'USD_rate')
def rate_USD(call):
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text=f'Курс продажу *{round(currency["buy"][0],2)}*\nКурс купівлі *{round(currency["sale"][0],2)}*',
                          parse_mode='Markdown'
                          )


@bot.callback_query_handler(func=lambda call: call.data == 'EUR_rate')
def rate_EUR(call):
    bot.edit_message_text(chat_id=call.message.chat.id,
                          message_id=call.message.id,
                          text=f'Курс продажу *{round(currency["buy"][1],2)}*\nКурс купівлі *{round(currency["sale"][1],2)}*',
                          parse_mode='Markdown'
                          )


@bot.callback_query_handler(func=lambda call: call.data == 'USD_to_UAH')
def step1(call):
    msg = bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.id,
                                text='Введіть суму в долларах, яку хочете обміняти')
    bot.register_next_step_handler(message=msg, callback=exchange_USD_to_UAH)


def exchange_USD_to_UAH(msg):
    try:
        usd = float(msg.text)
        bot.send_message(chat_id=msg.chat.id,
                         text=f'На {usd} долларів ви можете купити {round(usd * currency["sale"][0], 2)}грн',
                         reply_markup=keyboard.mainKeyboard()
                         )
    except ValueError:
        msg = bot.send_message(chat_id=msg.chat.id,
                               text=f'Треба ввести число. Спробуйте ще раз')
        bot.register_next_step_handler(message=msg, callback=exchange_USD_to_UAH)


@bot.callback_query_handler(func=lambda call: call.data == 'USD_to_EUR')
def step1(call):
    msg = bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.id,
                                text='Введіть суму в долларах, яку хочете обміняти')
    bot.register_next_step_handler(message=msg, callback=exchange_USD_to_EUR)


def exchange_USD_to_EUR(msg):
    try:
        usd = float(msg.text)
        bot.send_message(chat_id=msg.chat.id,
                         text=f'На {usd} долларів ви можете купити {round(usd * (currency["sale"][0]) / (currency["sale"][1]), 2)}eur',
                         reply_markup=keyboard.mainKeyboard()
                         )
    except ValueError:
        msg = bot.send_message(chat_id=msg.chat.id,
                               text=f'Треба ввести число. Спробуйте ще раз')
        bot.register_next_step_handler(message=msg, callback=exchange_USD_to_EUR)


@bot.callback_query_handler(func=lambda call: call.data == 'EUR_to_UAH')
def step1(call):
    msg = bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.id,
                                text='Введіть суму в євро, яку хочете обміняти')
    bot.register_next_step_handler(message=msg, callback=exchange_EUR_to_UAH)


def exchange_EUR_to_UAH(msg):
    try:
        eur = float(msg.text)
        bot.send_message(chat_id=msg.chat.id,
                         text=f'На {eur} євро ви можете купити {round(eur * currency["sale"][1], 2)}грн',
                         reply_markup=keyboard.mainKeyboard()
                         )
    except ValueError:
        msg = bot.send_message(chat_id=msg.chat.id,
                               text=f'Треба ввести число. Спробуйте ще раз')
        bot.register_next_step_handler(message=msg, callback=exchange_EUR_to_UAH)


@bot.callback_query_handler(func=lambda call: call.data == 'EUR_to_USD')
def step1(call):
    msg = bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.id,
                                text='Введіть суму в євро, яку хочете обміняти')
    bot.register_next_step_handler(message=msg, callback=exchange_EUR_to_USD)


def exchange_EUR_to_USD(msg):
    try:
        eur = float(msg.text)
        bot.send_message(chat_id=msg.chat.id,
                         text=f'На {eur} євро ви можете купити {round(eur * (currency["sale"][1]) / (currency["sale"][0]), 2)}usd',
                         reply_markup=keyboard.mainKeyboard()
                         )
    except ValueError:
        msg = bot.send_message(chat_id=msg.chat.id,
                               text=f'Треба ввести число. Спробуйте ще раз')
        bot.register_next_step_handler(message=msg, callback=exchange_EUR_to_USD)


@bot.callback_query_handler(func=lambda call: call.data == 'UAH_to_USD')
def step1(call):
    msg = bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.id,
                                text='Введіть суму в гривнях, яку хочете обміняти')
    bot.register_next_step_handler(message=msg, callback=exchange_UAH_to_USD)


def exchange_UAH_to_USD(msg):
    try:
        uah = float(msg.text)
        bot.send_message(chat_id=msg.chat.id,
                         text=f'На {uah} гривень ви можете купити {round(uah / currency["sale"][0], 2)}usd',
                         reply_markup=keyboard.mainKeyboard()
                         )
    except ValueError:
        msg = bot.send_message(chat_id=msg.chat.id,
                               text=f'Треба ввести число. Спробуйте ще раз')
        bot.register_next_step_handler(message=msg, callback=exchange_UAH_to_USD)


@bot.callback_query_handler(func=lambda call: call.data == 'UAH_to_EUR')
def step1(call):
    msg = bot.edit_message_text(chat_id=call.message.chat.id,
                                message_id=call.message.id,
                                text='Введіть суму в гривнях, яку хочете обміняти')
    bot.register_next_step_handler(message=msg, callback=exchange_UAH_to_EUR)


def exchange_UAH_to_EUR(msg):
    try:
        uah = float(msg.text)
        bot.send_message(chat_id=msg.chat.id,
                         text=f'На {uah} гривень ви можете купити {round(uah / currency["sale"][1], 2)}eur',
                         reply_markup=keyboard.mainKeyboard()
                         )
    except ValueError:
        msg = bot.send_message(chat_id=msg.chat.id,
                               text=f'Треба ввести число. Спробуйте ще раз')
        bot.register_next_step_handler(message=msg, callback=exchange_UAH_to_EUR)
