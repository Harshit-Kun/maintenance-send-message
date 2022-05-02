from pyrogram import Client, filters

bot = Client(
    "my first project",
    API_ID = 8424747,
    API_HASH = "8c1cf9dc795e9a2a69e80b068c8ad2a7",
    BOT_TOKEN = "5046696779:AAEOB3ojcT7vc9HaX15YUWrhJNKXaXmIugM"
)
@bot.on_message(filters.command('start') & filters.private)
 
def command1(bot, message):
    bot.on_message(message.chat.id, "Nezuko is in maintenance , so please wait till the bot start's again  ")

bot.run()
