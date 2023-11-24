import telebot
import random
from datetime import datetime

# Токен вашего бота
TOKEN = 'YOUR_BOT_TOKEN'

# Создание экземпляра бота
bot = telebot.TeleBot(TOKEN)

# Переменная с датами дня рождения
birthdays = {
    'Иван': '25.01',
    'Мария': '10.03',
    'Алексей': '15.06',
    'Елена': '05.09',
    'Андрей': '20.11'
}

# Фразы для поздравлений
greetings = [
    "С днем рождения! Пусть все твои мечты сбываются!",
    "Счастливого дня рождения! Желаю радости и улыбок на протяжении всего года!",
    "С днем рождения! Пусть этот день будет наполнен любовью и счастьем!",
    "Поздравляю с днем рождения! Желаю ярких эмоций и незабываемых моментов!"
]

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот-поздравлятор. Введите свое имя, чтобы я мог поздравить вас с днем рождения.")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def congratulate(message):
    name = message.text
    if name in birthdays:
        birthday = datetime.strptime(birthdays[name], "%d.%m")
        today = datetime.now().replace(year=datetime.now().year)

        # Проверяем, является ли сегодня день рождения пользователя
        if today == birthday:
            greeting = random.choice(greetings)
            bot.reply_to(message, f"{greeting} {name}!")
        else:
            bot.reply_to(message, f"Сегодня не твой день рождения, {name}.")
    else:
        bot.reply_to(message, "Извините, я не знаю вашего дня рождения.")

    # Запуск бота
    bot.polling()
