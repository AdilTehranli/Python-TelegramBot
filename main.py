import telebot
from telebot import types
# import webbrowser
bot = telebot.TeleBot('6856349827:AAFy-xklTBxguIutg6NuWK86LY9U0QS_4Gw')

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.InlineKeyboardMarkup('join site',url='https://google.com'))
    markup.add(types.InlineKeyboardMarkup('delete photo',callback_data='delete'))
    markup.add(types.InlineKeyboardMarkup('update text',callback_data='edit'))

    bot.reply_to(message,"very good",reply_markup=markup)

bot.polling(none_stop=True)


# @bot.message_handler(commands=['site','website'])
# def site(message):
#    webbrowser.open('https://itproger.com')
#
# @bot.message_handler(commands=['start'])
# def main(message):
#    bot.send_message(message.chat.id,f'Hello,{message.from_user.first_name},{message.from_user.last_name}')
#
# @bot.message_handler(commands=['help'])
# def main(message):
#    bot.send_message(message.chat.id, '<b>help</b> <u>information</u> about', parse_mode='html')
#
# @bot.message_handler()
# def info(message):
#    if message.text.lower() == 'hello':
#       bot.send_message(message.chat.id, f'Hello,{message.from_user.first_name},{message.from_user.last_name}')
#    elif message.text.lower() == 'id':
#       bot.send_message(message.chat.id, f'id: {message.from_user.id}')
