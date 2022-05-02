from pyrogram import Client, filters

bot = Client(
    "my first project",
    API_ID = ,
    API_HASH = "",
    BOT_TOKEN = ""
)
@bot.on_message(filters.command('start') & filters.private)
 
def command1(bot, message):
    bot.on_message(message.chat.id, "Nezuko is in maintenance , so please wait till the bot start's again  ")

bot.run()
