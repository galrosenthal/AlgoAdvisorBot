from typing import List

from telegram.ext import *
from telegram.ext.dispatcher import run_async
from telegram import BotCommand
import advisor as adv
import CONSTANTS
import logging as logger

# list of Available commands
AVAILABLE_COMMANDS = [
    {
        'name': 'start',
        'description': 'Start a new chat with the bot'
    },
    {
        'name': 'help',
        'description': 'Print the help message'
    },
    {
        'name': 'general',
        'description': 'General portfolio with multi field stocks'
    },
    {
        'name': 'health',
        'description': 'Health technology portfolio'
    },
    {
        'name': 'utils',
        'description': 'Utilities portfolio'
    },
    {
        'name': 'energy_minerals ',
        'description': 'Energy and Minerals portfolio'
    },
    {
        'name': 'finance',
        'description': 'Finance portfolio'
    },
    {
        'name': 'tech_services',
        'description': 'Technology services portfolio'
    }
]


def help_text():
    help_str = "\n\n\nWelcome to BotAdvisor,\n" \
               "This bot is advising you for the best trading portfolio " \
               "based on a specific field of interest, Technology, Health, etc." \
               "The supported commands:\n" \
               "1. /start - Start a new chat with the bot \n" \
               "2. /help - Print the help message \n" \
               "3. /general - General portfolio with multi field stocks\n" \
               "4. /health - Health technology portfolio\n" \
               "5. /utils - Utilities portfolio\n" \
               "6. /energy_minerals - Energy and Minerals portfolio\n" \
               "7. /finance - Finance portfolio\n" \
               "8. /tech_services - Technology services portfolio"
    return help_str

def start(update, context):
    logger.info('New Session Started')
    str_val = "Welcome " + str(update.message.chat_id) + ', Lets start'
    str_val += help_text()
    update.message.reply_text(str_val)


def help(update, context):
    logger.info("Help print")
    text = help_text()
    update.message.reply_text(text)


def general(update, context):
    logger.info('New general Question')
    tickers = ["SPY", "QQQ", "IEI", "LQD", "TA35.TA", "FB", "GOOGL", 'AMAZ']  # The Name Tiker
    adv.calculate_protfolio(tickers, update.message.chat_id, type='general')
    context.bot.sendPhoto(chat_id=update.message.chat.id, photo=open(str(update.message.chat_id) + '.png', 'rb'))


def health_tech(update, context):
    logger.info('New health_tech Question')
    tickers = ["COCP", "BLRX", "ADMP", "STIM", "TENX", "MTP", "VXRT", 'EDSA']  # The Name Tiker
    adv.calculate_protfolio(tickers, update.message.chat_id, type='health_tech')
    context.bot.sendPhoto(chat_id=update.message.chat.id, photo=open(str(update.message.chat_id) + '.png', 'rb'))


def utils(update, context):
    logger.info('New utils Question')
    tickers = ["ENIC", "AGR", "MDU", "HE", "CMSA", "AWR", "EDN", 'HNP']  # The Name Tiker
    adv.calculate_protfolio(tickers, update.message.chat_id, type='utils')
    context.bot.sendPhoto(chat_id=update.message.chat.id, photo=open(str(update.message.chat_id) + '.png', 'rb'))


def energy_minerals(update, context):
    logger.info('New energy_minerals Question')
    tickers = ["MTR", "BCEI", "CEIX", "INDO", "GBR", "PNRG", "ESTE", 'AR']  # The Name Tiker
    adv.calculate_protfolio(tickers, update.message.chat_id, type='energy_minerals')
    context.bot.sendPhoto(chat_id=update.message.chat.id, photo=open(str(update.message.chat_id) + '.png', 'rb'))


def finance(update, context):
    logger.info('New finance Question')
    tickers = ["VBFC", "XYF", "VINO", "TBBK", "VSPRU", "BRPAU", "ELVT", 'GMTX']  # The Name Tiker
    adv.calculate_protfolio(tickers, update.message.chat_id, type='finance')
    context.bot.sendPhoto(chat_id=update.message.chat.id, photo=open(str(update.message.chat_id) + '.png', 'rb'))


def tech_services(update, context):
    logger.info('New tech_services Question')
    tickers = ["JOBS", "CLST", "MOXC", "TKAT", "TZOO", "GB", 'TAOP']  # The Name Tiker
    adv.calculate_protfolio(tickers, update.message.chat_id, type='tech_services')
    context.bot.sendPhoto(chat_id=update.message.chat.id, photo=open(str(update.message.chat_id) + '.png', 'rb'))


def get_our_bot_commands():
    bot_commands: List[BotCommand] = []
    for command in AVAILABLE_COMMANDS:
        new_bot_command = BotCommand(command['name'], command['description'])
        bot_commands.append(new_bot_command)

    return bot_commands


def main():
    logger.basicConfig(level=logger.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%d/%m/%Y-%H:%M:%S')

    print("Starting....")
    updater = Updater(CONSTANTS.API_KEY, use_context=True, workers=6)

    dp = updater.dispatcher
    avail_bot_commands = get_our_bot_commands()
    dp.bot.set_my_commands(avail_bot_commands)
    dp.add_handler(CommandHandler('start', start, run_async=True))
    dp.add_handler(CommandHandler('help', help, run_async=True))
    dp.add_handler(CommandHandler('general', general, run_async=True))
    dp.add_handler(CommandHandler('health', health_tech, run_async=True))
    dp.add_handler(CommandHandler('utils', utils, run_async=True))
    dp.add_handler(CommandHandler('energy', energy_minerals, run_async=True))
    dp.add_handler(CommandHandler('finance', finance, run_async=True))
    dp.add_handler(CommandHandler('tech_services', tech_services, run_async=True))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()