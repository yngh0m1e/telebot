import telebot
from config import token

API_TOKEN = token

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, """\
                Помогите!!!
                Нет.\
""")

@bot.message_handler(commands=['fact'])
def send_fact(message):
    bot.reply_to(message, """\
            Жесть.\
""")

@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)

@bot.message_handler(commands=['joke'])
def send_joke(message):
    bot.reply_to(message, """\
            Иван-дурак приходит к царю:
— Я выполнил свое обещание, вот голова дракона. А ты выполнишь свое? 
— Да, вот рука принцессы.\
""")
    
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
