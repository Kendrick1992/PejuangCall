from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# Ambil token dari environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Handler /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Bot kamu sudah aktif 🎉")

# Setup aplikasi bot
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("🤖 Bot sedang berjalan...")
app.run_polling()