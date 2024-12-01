from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler

# Bot tokenini kiriting
TOKEN = '7657294573:AAEqJvZCa5lJemedhvL7cnGsgQGFykIgC6I'

async def start(update, context):
    """Foydalanuvchiga inline tugma yuborish"""
    keyboard = [
        [InlineKeyboardButton("Saytga o'tish", url="https://youtube.com")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # update.message obyektidan to'g'ri foydalanish
    await update.message.reply_text(
        'Botni ishga tushurdingiz! Saytga o\'tish uchun quyidagi tugmani bosing:',
        reply_markup=reply_markup
    )

def main():
    """Botni ishga tushirish"""
    # Application obyekti yaratish
    application = Application.builder().token(TOKEN).build()
    
    # /start komandasi uchun handler
    application.add_handler(CommandHandler("start", start))
    
    # Botni ishga tushurish
    application.run_polling()

if __name__ == '__main__':
    main()
