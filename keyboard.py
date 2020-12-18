from telebot import types


def tradeKeyboard():
    trade_keyboard = types.ReplyKeyboardMarkup(True, True)
    key4 = types.KeyboardButton('Обміник')
    key5 = types.KeyboardButton('Назад')
    trade_keyboard.add(key4)
    trade_keyboard.add(key5)

    return trade_keyboard


def mainKeyboard():

    main_keyboard = types.ReplyKeyboardMarkup(True, True)
    key1 = types.KeyboardButton('💲Курси валют💲')
    key2 = types.KeyboardButton('Обмін валют')

    main_keyboard.add(key1)
    main_keyboard.add(key2)

    return main_keyboard


def exchange_menu():

    exchange_menu = types.InlineKeyboardMarkup()
    key11 = types.InlineKeyboardButton(text='🇺🇸Доллар - гривня🇺🇦', callback_data='USD_to_UAH')
    key12 = types.InlineKeyboardButton(text='🇺🇸Доллар - Євро🇪🇺', callback_data='USD_to_EUR')
    key13 = types.InlineKeyboardButton(text='🇪🇺Євро - гривня🇺🇦', callback_data='EUR_to_UAH')
    key14 = types.InlineKeyboardButton(text='🇪🇺Євро - доллар🇺🇸', callback_data='EUR_to_USD')
    key15 = types.InlineKeyboardButton(text='🇺🇦Гривня - доллар🇺🇸', callback_data='UAH_to_USD')
    key16 = types.InlineKeyboardButton(text='🇺🇦Гривня - євро🇪🇺', callback_data='UAH_to_EUR')

    exchange_menu.add(key11)
    exchange_menu.add(key12)
    exchange_menu.add(key13)
    exchange_menu.add(key14)
    exchange_menu.add(key15)
    exchange_menu.add(key16)
    return exchange_menu


def rate_menu():
    rate_menu = types.InlineKeyboardMarkup()
    key17 = types.InlineKeyboardButton(text='🇺🇸Курс доллар🇺🇸', callback_data='USD_rate')
    key18 = types.InlineKeyboardButton(text='🇪🇺Курс євро🇪🇺', callback_data='EUR_rate')
    key19 = types.InlineKeyboardButton(text='🇺🇳Всі валюти🇺🇳', callback_data='All_rate')

    rate_menu.add(key17)
    rate_menu.add(key18)
    rate_menu.add(key19)

    return rate_menu
