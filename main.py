import telebot
import webbrowser
bot = telebot.TeleBot('6856349827:AAFy-xklTBxguIutg6NuWK86LY9U0QS_4Gw')

@bot.message_handler(commands=['site','website'])
def site(message):
   webbrowser.open('https://itproger.com')

@bot.message_handler(commands=['start'])
def main(message):
   bot.send_message(message.chat.id,f'Hello,{message.from_user.first_name},{message.from_user.last_name}')

@bot.message_handler(commands=['help'])
def main(message):
   bot.send_message(message.chat.id, '<b>help</b> <u>information</u> about', parse_mode='html')

@bot.message_handler()
def info(message):
   if message.text.lower() == 'hello':
      bot.send_message(message.chat.id, f'Hello,{message.from_user.first_name},{message.from_user.last_name}')
   elif message.text.lower() == 'id':
      bot.send_message(message.chat.id, f'id: {message.from_user.id}')


bot.polling(none_stop=True)