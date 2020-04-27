#import telebot
import psycopg2
import requests
from lib.settings import token, add_corona, Show_Cases, Connect_to_Database

URL = "https://api.covid19api.com/summary"


def func(URL):
    response = requests.get(URL)
    return response.json()


Covid = requests.get(URL)
Covid = Covid.json()


def Update_db(Covid):
    for item in Covid["Countries"]:
        Country = item["Country"]
        Slug = item["Slug"]
        NewConfirmed = item["NewConfirmed"]
        TotalConfirmed = item["TotalConfirmed"]
        NewDeaths = item["NewDeaths"]
        TotalDeaths = item["TotalDeaths"]
        NewRecovered = item["NewRecovered"]
        TotalRecovered = item["TotalRecovered"]
        add_corona(Country, Slug, NewConfirmed, TotalConfirmed,
                   NewDeaths, TotalDeaths, NewRecovered, TotalRecovered)


def Menu(Covid):
    exit = True
    while exit:
        print("If you are launching the programe for the first time Enter ( 1 ), if NOT , follow the instructions!\n ")
        choice = int(
            input("1.Getting things together\n2.Show Cases \t0. EXIT => "))
        if choice == 1:
            print("Creating database please wait :  ")
            Connect_to_Database()
            Show_Cases()
            print("Gathering information from the source for you :")
            # fill_in(Covid_19)
            print("Info has been added to database Successfully!")
        elif choice == 2:
            print("Loading ...")
            Show_Cases()
        elif choice == 0:
            exit = False


Menu(Covid)


"""bot = telebot.TeleBot(token)


@bot.message_handler(commands=['about', 'help', 'start'])
def hendler_command(command):
    print("command => ", command)
    if command.text == "/about":
        bot.send_message(
            command.chat.id, "Моніторинг ситуації із кількістю госпіталізованих осіб з підозрою та підтвердженими випадками захворювання на COVID-19")
    elif command.text == "/help" or command.text == "/start":
        bot.send_message(command.chat.id, "Enter country name: ")


@bot.message_handler(content_types=["text"])
def handler_text(message):
    if message.text == "Rome":
        bot.send_message(message.chat.id, "COVID 19 1231 Rome")
    else:
        bot.send_message(message.chat.id, "Use /help for manual")


bot.polling(none_stop=True)"""
