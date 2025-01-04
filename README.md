# Telegram History Analyzer :robot:
*Provide accurate data about most used words, emojis and activity using json data from Telegram accound*

## MENU:
1. [Features](#features)
2. [Example](#example)
3. [Before Launching](#before-launching)
4. [How to RUN](#how-to-run)
6. [Dependencies](#dependencies)

## Features:
1. **Most used words** (Reveals TOP 10 most used words by user and depicts via bar chart)
2. **Most used EMOJIS**
3. **Compares activity of user in each month** (students&unknown_faces)
4. **Compares activity in each day of the week**
5. **Compares the activity in different timeframes** (midnight, morning, evening, etc.)
6. **Shows TOP people with highest activity**
7. **Dockerized container**


## Example:
![monthly_activity](https://i.postimg.cc/Z5Mzcvhm/monthly-activity.png)
![tg_bot](https://i.postimg.cc/B6W9WW6w/image.png)

## BEFORE LAUNCHING
1. Make sure you have python and pip installed
2. change the TOKEN variable inside ```install.py``` to the TOKEN of your bot
3. Recommended: install DOCKER

## HOW TO RUN:
**VIA DOCKER** :whale: : Open terminal and navigate to the repository folder. RUN ```docker compose up```

> [!NOTE]
> You can run the project without docker. To do so you will only need to run ```setup.bat``` (for Windows) or ```setup.sh``` on MacOS/Linux

## Customizing bot
> You can change the layout of inline buttons bot by modifying ```bot_settings.py``` file

## Dependencies:
```
matplotlib
telebot (pyTelegramBot)
```

Build and developed by Nurmuhammad Abdullaev

Thank you )
