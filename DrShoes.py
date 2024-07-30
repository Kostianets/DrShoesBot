from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CallbackContext, CommandHandler, CallbackQueryHandler 
import pandas as pd

TOKEN = '5972314664:AAFt3BimlGFnHrF-wmtXcb1S7lAzTfaTOCo'
#TODO: replace ID
MANAGER = "Pudgesf" 

updater = Updater(TOKEN)

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Послуги", callback_data='services')], #InlineKeyboardButton('Ціни', callback_data='prices')],
        [InlineKeyboardButton("Поширені запитання", callback_data='questions')],
        [InlineKeyboardButton("Налаштування", callback_data='settings')],
        [InlineKeyboardButton("Зв'язатися з менеджером", url=f"https://t.me/{MANAGER}")],
        [InlineKeyboardButton("Перевірити статус замовлення", callback_data='status')]
    ]
    
    reply_keyboard = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text('Вітаємо в боті DrShoes!', reply_markup=reply_keyboard)
    
def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    
    if query.data == 'services':
        keyboard = [
            [InlineKeyboardButton("Послуга 1", callback_data='service 1'), InlineKeyboardButton("Послуга 2", callback_data='service 2')],
            [InlineKeyboardButton("Послуга 3", callback_data='service 3'), InlineKeyboardButton("Послуга 4", callback_data='service 4')],
            [InlineKeyboardButton("<< Поверутися назад", callback_data='return1')]
        ]
        
        reply_keyboard = InlineKeyboardMarkup(keyboard)

        query.edit_message_text('Тестове повідомлення', reply_markup=reply_keyboard)
    
    if query.data == 'questions':
        keyboard = [
            [InlineKeyboardButton("Запитання 1", callback_data='question 1'), InlineKeyboardButton("Запитання 2", callback_data='question 2')],
            [InlineKeyboardButton("Запитання 3", callback_data='question 3'), InlineKeyboardButton("Запитання 4", callback_data='question 4')],
            [InlineKeyboardButton("<< Поверутися назад", callback_data='return1')]
        ]
        
        reply_keyboard = InlineKeyboardMarkup(keyboard)

        query.edit_message_text('Тестове повідомлення', reply_markup=reply_keyboard)
        
    if query.data == 'settings':
        keyboard = [
            [InlineKeyboardButton('Мова', callback_data='lang')],
            [InlineKeyboardButton('<< Повернутися назад', callback_data='return1')]
        ]
        
        reply_keyboard = InlineKeyboardMarkup(keyboard)

        query.edit_message_text('Тестове повідомлення', reply_markup=reply_keyboard)
    
    if query.data == 'status':
        keyboard = [
            [InlineKeyboardButton('<< Повернутися назад', callback_data='return1')]
        ]
        
        query.edit_message_caption('Введіть номер замовлення:', reply_markup=reply_keyboard)
    
    if query.data == 'return1':
        keyboard = [
            [InlineKeyboardButton("Послуги", callback_data='services')], #InlineKeyboardButton('Ціни', callback_data='prices')],
            [InlineKeyboardButton("Поширені запитання", callback_data='questions')],
            [InlineKeyboardButton("Налаштування", callback_data='settings')],
            [InlineKeyboardButton("Зв'язатися з менеджером", url=f"https://t.me/{MANAGER}")]
        ]

        reply_keyboard = InlineKeyboardMarkup(keyboard)

        query.edit_message_text('Вітаємо в боті DrShoes!', reply_markup=reply_keyboard)

def main():
    #update_queue = None
    dispatcher = updater.dispatcher
    
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(button))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()