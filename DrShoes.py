from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, WebAppData
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
import pandas as pd

TOKEN = '5972314664:AAFt3BimlGFnHrF-wmtXcb1S7lAzTfaTOCo'
#TODO: replace ID
MANAGER = "Pudgesf" 
#TODO: rename file
file = pd.read_excel('file.xlsx')

updater = Updater(TOKEN)

def welcome_message(update: Update, context: CallbackContext):
    update.message.reply_text('Вітаємо в боті DrShoes!', reply_markup=main_menu())

def main_menu():
    keyboard = [
        [KeyboardButton("Послуги"), KeyboardButton("Поширені запитання")],
        [KeyboardButton("Налаштування"), KeyboardButton("Перевірити статус замовлення")],
        [KeyboardButton("Зв'язатися з менеджером")]
    ]
    
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def button(update: Update, context: CallbackContext):
    text = update.message.text
    # chat_id = update.message.chat_id
    # message_id = update.message.message_id
    
    match text:
        case "Послуги":
            update.message.reply_text('Наші послуги:', reply_markup=services())
        case "Налаштування":
            update.message.reply_text('Налаштування:', reply_markup=settings())
        case "Поширені запитання":
            update.message.reply_text("Запитання:", reply_markup=faq())
        case "Зв'язатися з менеджером":
            update.message.reply_text(f"З менеджером можете зв'язатися за цим посиланням: @{MANAGER}")
        case "<< Повернутися назад":
            update.message.reply_text('Вітаємо в боті DrShoes!', reply_markup=main_menu())
        case _:
            update.message.reply_text("Будь ласка, оберіть один з варіантів:", reply_markup=main_menu())

def services():
    keyboard = [
        [KeyboardButton("Послуга 1"), KeyboardButton("Послуга 2")],
        [KeyboardButton("Послуга 3"), KeyboardButton("Послуга 4")],
        [KeyboardButton("<< Повернутися назад")]
    ]
    
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def settings():
    keyboard = [
        [KeyboardButton("Мова")],
        [KeyboardButton("<< Повернутися назад")]
    ]
    
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def faq():
    keyboard = [
        [KeyboardButton("Запитання 1"), KeyboardButton("Запитання 2")],
        [KeyboardButton("Запитання 3"), KeyboardButton("Запитання 4")],
        {KeyboardButton("<< Повернутися назад")}
    ]
    
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def main():
    #update_queue = None
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler('start', welcome_message))
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, button))

    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()