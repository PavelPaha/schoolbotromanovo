import telebot
import config
import datetime
import random

now = datetime.datetime.now()
password = False
from telebot import types
bot = telebot.TeleBot(config.TOKEN)

tt = []
ttstr = 'Пусто('
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Завтрашнее расписание")
    markup.add(item1)
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот, который умеет отправлять Вам расписание уроков 10 класса!".format(message.from_user,bot.get_me()),
        parse_mode='html', reply_markup = markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    global password
    global ttstr
    global tt
    data = 0
    if message.chat.type == 'private': #пароль для в хода в подвал бота
        data = now.day
        
        if message.text == '1xerrd':
            password = True
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton("Обновить завтрашнее расписание")
            item2 = types.KeyboardButton("Посмотреть расписание")
            item3 = types.KeyboardButton("Очистить расписание")


            markup.add(item1, item2, item3)
            bot.send_message(message.chat.id, 'Добро пожаловать в подвал. Что хотите сделать: ', reply_markup = markup)

        elif message.text == 'Обновить завтрашнее расписание' and password: # доступно при пароле


            ttstr = 'Пусто('

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Русский язык", callback_data='Русский язык')
            item2 = types.InlineKeyboardButton("Математика", callback_data='Математика')
            item3 = types.InlineKeyboardButton("Литература", callback_data='Литература')
            item4 = types.InlineKeyboardButton("Физика", callback_data='Физика')
            item5 = types.InlineKeyboardButton("Информатика", callback_data='Информатика')
            item6 = types.InlineKeyboardButton("Немецкий язык", callback_data='Немецкий язык')
            item7 = types.InlineKeyboardButton("Астрономия", callback_data='Астрономия')
            item8 = types.InlineKeyboardButton("Физ-ра", callback_data='Физ-ра')
            item9 = types.InlineKeyboardButton("ОБЖ", callback_data='ОБЖ')
            item10 = types.InlineKeyboardButton("История", callback_data='История')
            item11 = types.InlineKeyboardButton("Обществознание", callback_data='Обществознание')
            item12 = types.InlineKeyboardButton("Химия", callback_data='Химия')
            item13 = types.InlineKeyboardButton("Рус КАТ", callback_data='Рус КАТ')
            item14 = types.InlineKeyboardButton("МХК", callback_data='МХК')
            item15 = types.InlineKeyboardButton("География", callback_data='География')
            item16 = types.InlineKeyboardButton("Английский язык", callback_data='Английский язык')
            markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12, item13, item14, item15, item16)
            bot.send_message(message.chat.id, 'Добавьте предметы', reply_markup = markup)
        elif message.text == 'Завтрашнее расписание' or message.text == "Посмотреть расписание":
            bot.send_message(message.chat.id, ttstr)
        elif message.text == "Очистить расписание":
            ttstr = 'Пусто...'
            bot.send_message(message.chat.id, ttstr)
        elif data != now.day:
            ttstr = 'Пустоо'
        elif message.text == 'Спасибо':
            number = random.randint(1, 6)
            if number == 1:
                bot.send_message(message.chat.id, 'Пожалуйста)')
            elif number == 2:
                bot.send_message(message.chat.id, 'Обращайся')
            elif number == 3:
                bot.send_message(message.chat.id, 'Тебе спасибо, милота)')
            elif number == 4:
                bot.send_message(message.chat.id, 'На здоровье')
            else: 
                bot.send_message(message.chat.id, 'Если нужно будет ещё расписание, жми на кнопку снизу!')
        else:
            bot.send_message(message.chat.id, 'Я пока не умею отвечать на этот запрос. Мой ПОВЕЛИТЕЛЬ вскоре добавит эту возможность... Ладно?')
        

   
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global tt
    global ttstr
    try:
        if call.message:
            if call.data == 'Русский язык':
                tt.append('Русский язык')
                bot.send_message(call.message.chat.id, 'Выполнено')

            elif call.data == 'Математика':
                tt.append('Математика')
                bot.send_message(call.message.chat.id, 'Выполнено')

            elif call.data == 'Литература':
                tt.append('Литература')
                bot.send_message(call.message.chat.id, 'Выполнено')

            elif call.data == 'Физика':
                tt.append('Физика')
                bot.send_message(call.message.chat.id, 'Выполнено')

            elif call.data == 'Информатика':
                tt.append('Информатика')
                bot.send_message(call.message.chat.id, 'Выполнено')

            elif call.data == 'Немецкий язык':
                tt.append('Немецкий язык')
                bot.send_message(call.message.chat.id, 'Выполнено')

            elif call.data == 'Астрономия':
                tt.append('Астрономия')
                bot.send_message(call.message.chat.id, 'Выполнено')

            elif call.data == 'Физ-ра':
                tt.append('Физ-ра')
                bot.send_message(call.message.chat.id, 'Выполнено')

            elif call.data == 'ОБЖ':
                tt.append('ОБЖ')
                bot.send_message(call.message.chat.id, 'Выполнено')

            elif call.data == 'История':
                tt.append('История')
                bot.send_message(call.message.chat.id, 'Выполнено')

            elif call.data == 'Обществознание':
                tt.append('Обществознание')
                bot.send_message(call.message.chat.id, 'Выполнено')

            elif call.data == 'Химия':
                tt.append('Химия')
                bot.send_message(call.message.chat.id, 'Выполнено')

            elif call.data == 'Рус КАТ':
                tt.append('Рус КАТ')
                bot.send_message(call.message.chat.id, 'Выполнено')

            elif call.data == 'МХК':
                tt.append('МХК')
                bot.send_message(call.message.chat.id, 'Выполнено')

            elif call.data == 'География':
                tt.append('География')
                bot.send_message(call.message.chat.id, 'Выполнено')

            elif call.data == 'Английский язык':
                tt.append('Английский язык')
                bot.send_message(call.message.chat.id, 'Выполнено')
            else:
                bot.send_message(call.message.chat.id, 'Ошибка. Данного предмета или команды нет(')

            ttstr = ', '.join(tt)
            #remove inline buttons
            #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ага",
            #    reply_markup=None)

            #bot.answer_callback_query(chat_id=call.message.chat.id, show_alert=False,
            #    text = "Это тестовое уведомление")
    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)
