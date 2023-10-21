# ktime_converter_bot

This is a Telegram bot to convert the most knowed timezones to Mexico City Hour. 
It's for personal use, but you can use it and deploy it on your own.

## Suported timezones
### America
* EST
* PST
* UTC
* CST
* EDT
  
### Europe
* CET

### Africa
* CAT

### Asia
* HKT
* JST
* KST

### Australia
* AEST

## Setup instructions
The setup instructions are on the requirements.txt file, but also here:
### If you don't want to use virtual environment
1. pip install python-telegram-bot==13.3
2. python main.py

### If you want to use virtual environment (recommended, tested in Arch Linux, it can be a little different in other OS)
1. python3 -m virtualenv venv
2. source venv/bin/activate
3. pip install python-telegram-bot==13.3
4. python main.py

### Notes
* Make sure you install python-telegram-bot's 13.3, in other versions it may not works correctly.
