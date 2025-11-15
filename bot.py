from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8028282752:AAFRk4awNcyLtWMYvDd5vhNxttpPPaP2H0k"
# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот, который помогает тебе получать лучшие промпты и гайды по нейросетям 🤖.\nНапиши /help, чтобы увидеть все команды."
    )

# /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Вот что я умею:\n"
        "/start – начать работу\n"
        "/music – промпты для Suno AI 🎧\n"
        "/video – гайд по HeyGen 🎥\n"
        "/guide – чек-листы и инструкции 📋\n"
        "/support – поддержка 💬\n"
        "/faq – часто задаваемые вопросы ❓\n"
        "/promo – текущие акции 🔥\n"
        "/new – нейросеть недели 🚀\n"
        "/packs – все доступные наборы 📦"
    )

# /music
async def music(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎧 PDF «10 промптов для Suno AI»\nЦена: 149 грн\nОплата: https://your-payment-link.com\nПосле оплаты я пришлю файл!"
    )

# /video
async def video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎥 Гайд по HeyGen: как делать видео с аватаром и озвучкой.\nСкоро доступен!"
    )

# /guide
async def guide(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 Чек-листы и инструкции:\n– Как формулировать промпты\n– Как улучшать треки\n– Как использовать Suno и HeyGen вместе"
    )

# /support
async def support(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💬 Поддержка: напиши @your_support_handle, я помогу!"
    )

# /faq
async def faq(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "❓ Часто задаваемые вопросы:\n– Как оплатить?\n– Когда придёт файл?\n– Что делать, если бот не отвечает?"
    )

# /promo
async def promo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Акция недели: при покупке Suno PDF — бонусный гайд по HeyGen бесплатно!"
    )

# /new
async def new(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Нейросеть недели: Suno AI — создаёт музыку по тексту. Напиши /music, чтобы получить промпты."
    )

# /packs
async def packs(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📦 Доступные наборы:\n– Suno AI промпты\n– HeyGen гайд\n– Чек-листы по нейросетям\nНапиши /music или /video, чтобы получить."
    )
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("music", music))
    app.add_handler(CommandHandler("video", video))
    app.add_handler(CommandHandler("guide", guide))
    app.add_handler(CommandHandler("support", support))
    app.add_handler(CommandHandler("faq", faq))
    app.add_handler(CommandHandler("promo", promo))
    app.add_handler(CommandHandler("new", new))
    app.add_handler(CommandHandler("packs", packs))

    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
