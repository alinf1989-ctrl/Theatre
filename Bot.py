import telebot

# 🔑 اینجا توکن رباتی که از BotFather گرفتی رو بذار
API_TOKEN = "8445893584"

bot = telebot.TeleBot(API_TOKEN)

# 🎭 لیست جشنواره‌های تئاتر ایران (موقت – بعدا میشه آنلاین کرد)
festivals = [
    "🎭 جشنواره بین‌المللی فجر – اعلام فراخوان: 1 مهر 1404",
    "🎭 جشنواره تئاتر خیابانی شهروند – اعلام فراخوان: 11 خرداد 1404",
    "🎭 جشنواره تئاتر کودک و نوجوان – اعلام فراخوان: 11 اردیبهشت 1404",
    "🎭 جشنواره تئاتر دانشگاهی – اعلام فراخوان: 12 فروردین 1404"
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام 👋 من ربات جشنواره‌های تئاتر هستم.\n"
                          "برای دیدن لیست جشنواره‌ها دستور /festivals رو بزن.")

@bot.message_handler(commands=['festivals'])
def send_festivals(message):
    response = "\n\n".join(festivals)
    bot.reply_to(message, "📅 لیست جشنواره‌ها:\n\n" + response)

print("🤖 Bot is running...")
bot.polling(none_stop=True)
