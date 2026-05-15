from telegram import *
from telegram.ext import *
import os

TOKEN = os.getenv("TOKEN")
async def start(update, context):
    buttons = [
        [InlineKeyboardButton("➕ Cargar saldo", callback_data="saldo"),
         InlineKeyboardButton("💰 Mi saldo", callback_data="misaldo")],

        [InlineKeyboardButton("🛒 Comprar cuentas", callback_data="comprar")],

        [InlineKeyboardButton("🆘 Soporte", callback_data="soporte")]
    ]

    await update.message.reply_text(
        "👤 BIENVENIDO AL PANEL USUARIO",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("BOT ONLINE")
app.run_polling()