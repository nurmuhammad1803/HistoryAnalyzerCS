import telebot
import json
import os
import matplotlib.pyplot as plt
from install import TOKEN
from bot_settings import main_menu

bot = telebot.TeleBot(TOKEN)

SAVE_DIR = "data/downloads/"
IMAGE_DIR = "data/images/"

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

user_files = {}

def analyze_top_words(file_path, user_id):
    with open(file_path, 'r', encoding="UTF-8") as file:
        data = json.load(file)

    answer = {}
    for item in data["chats"]["list"]:
        if item["type"] == "personal_chat":
            for text in item["messages"]:
                line = []
                if "text_entities" in text and text["text_entities"]:
                    line = str(text["text_entities"][0]["text"]).split()
                elif "text" in text and text["text"]:
                    line = str(text["text"]).split()
                for word in line:
                    answer[word] = answer.get(word, 0) + 1

    top = {k: v for k, v in sorted(answer.items(), key=lambda item: item[1], reverse=True)[:10]}

    keys = list(top.keys())
    values = list(top.values())
    plt.figure(figsize=(8, 5))
    plt.bar(keys, values, color='skyblue')
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.title("Top 10 Words sent in personal messages")
    image_path = os.path.join(IMAGE_DIR, "word_frequency.png")
    plt.savefig(image_path, dpi=300)
    plt.close()

    return [image_path, top]

def analyze_top_users(file_path):
    with open(file_path, 'r', encoding="UTF-8") as file:
        data = json.load(file)

    top_contacts = {}
    for item in data["frequent_contacts"]["list"]:
        if item["category"] == "people" and len(top_contacts.keys()) < 6:
            top_contacts[item["name"]] = item["rating"]

    sorted_contacts = {k: v for k, v in sorted(top_contacts.items(), key=lambda item: item[1], reverse=True)}

    names = list(sorted_contacts.keys())
    ratings = list(sorted_contacts.values())

    plt.figure(figsize=(10, 6))
    plt.bar(names, ratings, color='coral')
    plt.xlabel("Contacts")
    plt.ylabel("Rating")
    plt.title("Top 5 Frequent Contacts")
    plt.xticks(rotation=45, ha="right")

    image_path = os.path.join(IMAGE_DIR, "top_users_vertical.png")
    plt.tight_layout()
    plt.savefig(image_path, dpi=300)
    plt.close()

    return [image_path, sorted_contacts]


    return {}

def analyze_top_emojis(file_path):
    with open(file_path, 'r', encoding="UTF-8") as file:
        data = json.load(file)
    emojis = {}
    for item in data["chats"]["list"]:
        for text in item["messages"]:
            if "sticker_emoji" in text:
                emoji = text["sticker_emoji"]
                emojis[emoji] = emojis.get(emoji, 0) + 1

    top = {k: v for k, v in sorted(emojis.items(), key=lambda item: item[1], reverse=True)[:15]}

    labels = list(top.keys())
    sizes = list(top.values())
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, textprops={'fontsize': 10})
    plt.title("Top 15 Emojis Used")
    plt.axis('equal')

    image_path = os.path.join(IMAGE_DIR, "emojis_pie.png")
    plt.savefig(image_path, dpi=300)
    plt.close()

    return [image_path, top]

def analyze_activity_month(file_path):
    import calendar

    with open(file_path, 'r', encoding="UTF-8") as file:
        data = json.load(file)
    months = {month: 0 for month in calendar.month_name[1:]}

    for item in data["chats"]["list"]:
        for text in item["messages"]:
            month_number = int(text["date"][5:7])
            month_name = calendar.month_name[month_number]
            months[month_name] += 1

    month_names = list(months.keys())
    message_counts = list(months.values())

    plt.figure(figsize=(10, 6))
    plt.plot(month_names, message_counts, marker="o", color="dodgerblue", linestyle="--")
    plt.fill_between(month_names, message_counts, color="lightblue", alpha=0.4)
    plt.xlabel("Months")
    plt.ylabel("Number of Messages")
    plt.title("Messages Sent Each Month")
    plt.xticks(rotation=45, ha="right")

    image_path = os.path.join(IMAGE_DIR, "monthly_activity.png")
    plt.tight_layout()
    plt.savefig(image_path, dpi=300)
    plt.close()

    return [image_path, months]

def analyze_activity_weekdays(file_path):
    import calendar
    from datetime import datetime

    with open(file_path, 'r', encoding="UTF-8") as file:
        data = json.load(file)

    weekdays = {day: 0 for day in calendar.day_name}

    for item in data["chats"]["list"]:
        for text in item["messages"]:
            date_string = text["date"][:10]
            weekday = calendar.day_name[datetime.strptime(date_string, "%Y-%m-%d").weekday()]
            weekdays[weekday] += 1

    weekday_names = list(weekdays.keys())
    message_counts = list(weekdays.values())

    plt.figure(figsize=(10, 6))
    plt.plot(weekday_names, message_counts, marker="o", color="orange", linestyle="--")
    plt.fill_between(weekday_names, message_counts, color="peachpuff", alpha=0.4)
    plt.xlabel("Days of the Week")
    plt.ylabel("Number of Messages")
    plt.title("Messages Sent Each Day of the Week")
    plt.xticks(rotation=45, ha="right")

    image_path = os.path.join(IMAGE_DIR, "weekday_activity.png")
    plt.tight_layout()
    plt.savefig(image_path, dpi=300)
    plt.close()

    top_path = [image_path, weekdays] 
    return top_path

def analyze_activity_timeframes(file_path):
    from datetime import datetime

    with open(file_path, 'r', encoding="UTF-8") as file:
        data = json.load(file)

    timeframes = {
        "00:00 - 06:00": 0,
        "06:00 - 12:00": 0,
        "12:00 - 15:00": 0,
        "15:00 - 18:00": 0,
        "18:00 - 21:00": 0,
        "21:00 - 00:00": 0,
    }

    total_messages = 0 

    for item in data["chats"]["list"]:
        for text in item["messages"]:
            time_string = text["date"][11:16]
            hour = int(time_string[:2])
            total_messages += 1

            if 0 <= hour < 6:
                timeframes["00:00 - 06:00"] += 1
            elif 6 <= hour < 12:
                timeframes["06:00 - 12:00"] += 1
            elif 12 <= hour < 15:
                timeframes["12:00 - 15:00"] += 1
            elif 15 <= hour < 18:
                timeframes["15:00 - 18:00"] += 1
            elif 18 <= hour < 21:
                timeframes["18:00 - 21:00"] += 1
            elif 21 <= hour < 24:
                timeframes["21:00 - 00:00"] += 1

    timeframes_percent = {k: (v / total_messages) * 100 for k, v in timeframes.items()}

    labels = list(timeframes_percent.keys())
    sizes = list(timeframes_percent.values())
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']

    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors, wedgeprops={'edgecolor': 'black'})
    plt.title("Messages Sent by Time Frames (Percentages)")

    image_path = os.path.join(IMAGE_DIR, "timeframe_activity_pie.png")
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(image_path, dpi=300)
    plt.close()

    return [image_path, timeframes]



@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(
        message.chat.id, 
        "Welcome to History Analyzer Bot!👋 Please send your `result.json` file from exported Telegram Data to proceed."
    )

@bot.message_handler(content_types=['document'])
def handle_document(message):
    try:
        file_id = message.document.file_id
        file_info = bot.get_file(file_id)
        file_path = file_info.file_path
        downloaded_file = bot.download_file(file_path)

        save_path = os.path.join(SAVE_DIR, message.document.file_name)
        with open(save_path, "wb") as new_file:
            new_file.write(downloaded_file)

        user_files[message.chat.id] = save_path

        bot.send_message(message.chat.id, "✅ File uploaded successfully! Choose an action:", reply_markup=main_menu())
    except Exception as e:
        bot.reply_to(message, f"An error occurred ❗️: {str(e)}")

@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call):
    user_id = call.message.chat.id
    if user_id not in user_files:
        bot.answer_callback_query(call.id, "Please upload your `result.json` file first 📂")
        return

    file_path = user_files[user_id]

    if call.data == 'top_words':
        try:
            chart_path = analyze_top_words(file_path, user_id)
            print(chart_path)
            with open(chart_path[0], "rb") as chart:
                string_top = ''    
                for k, v in chart_path[1].items():
                    string_top += f"\n\t {k} - {v} times"
                bot.send_photo(call.message.chat.id, chart, caption=f"Here is the word frequency chart ! ⌨️ and detailed frequency (words you used the most): {string_top}")
        except Exception as e:
            bot.send_message(call.message.chat.id, f"🤨🚫 An error occurred: {str(e)}")      
    elif call.data == 'top_users':
        try:
            chart_path = analyze_top_users(file_path)
            print(chart_path)
            with open(chart_path[0], "rb") as chart:
                string_top = ''    
                for k, v in chart_path[1].items():
                    string_top += f"\n\t {k} - Rating: {v}"
                bot.send_photo(call.message.chat.id, chart, caption=f"Here are your TOP friends (take care of them) 😉! \nAnd detailed figures (in case you are interested): {string_top}")
        except Exception as e:
            bot.send_message(call.message.chat.id, f"An error occurred: {str(e)}")
    elif call.data == 'top_emojis':
        try:
            chart_path = analyze_top_emojis(file_path)
            print(chart_path)
            with open(chart_path[0], "rb") as chart:
                string_top = ''    
                for k, v in chart_path[1].items():
                    string_top += f"\n\t {k} - {v} times"
                bot.send_photo(call.message.chat.id, chart, caption=f"Here are your most used emojis! 🤓 \nAnd in numbers: {string_top}")
        except Exception as e:
            bot.send_message(call.message.chat.id, f"An error occurred: {str(e)}")     
    elif call.data == 'activity_month':
        try:
            chart_path = analyze_activity_month(file_path)
            print(chart_path)
            with open(chart_path[0], "rb") as chart:
                string_top = ''    
                for k, v in chart_path[1].items():
                    string_top += f"\n\t {k} - {v} times"
                bot.send_photo(call.message.chat.id, chart, caption=f"Here is the graph of your activity in each month! 📊 \n {string_top}")
        except Exception as e:
            bot.send_message(call.message.chat.id, f"An error occurred: {str(e)}")
    elif call.data == 'activity_weekdays':
        try:
            chart_path = analyze_activity_weekdays(file_path)
            print(chart_path)
            with open(chart_path[0], "rb") as chart:
                string_top = ''    
                for k, v in chart_path[1].items():
                    string_top += f"\n\t {k} - {v} times"
                bot.send_photo(call.message.chat.id, chart, caption=f"Here is the graph of your activity in each day of the week! 📊 \n {string_top}")
        except Exception as e:
            bot.send_message(call.message.chat.id, f"An error occurred: {str(e)}")
    elif call.data == 'activity_timeframes':
        try:
            chart_path = analyze_activity_timeframes(file_path)
            print(chart_path)
            with open(chart_path[0], "rb") as chart:
                string_top = ''    
                for k, v in chart_path[1].items():
                    string_top += f"\n\t Time frame: {k} -> {v}"
                bot.send_photo(call.message.chat.id, chart, caption=f"Here is the graph of your activity in different period of day! 📊 \n {string_top}")
        except Exception as e:
            bot.send_message(call.message.chat.id, f"An error occurred: {str(e)}")
    elif call.data == 'quit':
        bot.send_message(call.message.chat.id, "Goodbye! 👋😎")
    else:
        bot.send_message(call.message.chat.id, "Invalid option! 🤨🚫")

print("Bot is running...")
bot.polling(non_stop=True)