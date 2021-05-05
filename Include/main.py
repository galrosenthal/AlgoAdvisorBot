from telegram.ext import *
from telegram.ext.dispatcher import run_async
import advisor as adv
import CONSTANTS
import logging as logger


def start(update, context):
    # TODO: Add explaination of the bot
    logger.info('New Session Started')
    str_val = "Welcome " + str(update.message.chat_id) + ', Lets start'
    update.message.reply_text(str_val)

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


def main():
    logger.basicConfig(level=logger.INFO, format='%(asctime)s | %(levelname)s | %(message)s', datefmt='%d/%m/%Y-%H:%M:%S')

    print("Starting....")
    updater = Updater(CONSTANTS.API_KEY, use_context=True, workers=6)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start, run_async=True))
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