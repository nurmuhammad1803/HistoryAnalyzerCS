from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Top Words ⌨️", callback_data='top_words'),
        InlineKeyboardButton("Top Users 👤", callback_data='top_users'),
        InlineKeyboardButton("Top Emojis 🎨", callback_data='top_emojis'),
        InlineKeyboardButton("Activity by Month ⚜️", callback_data='activity_month'),
        InlineKeyboardButton("Activity by Days of the week 📆", callback_data='activity_weekdays'),
        InlineKeyboardButton("Activity by Time Frames ⏰", callback_data='activity_timeframes'),
        InlineKeyboardButton("Quit", callback_data='quit')
    )
    return markup