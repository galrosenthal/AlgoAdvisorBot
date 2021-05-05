from telegram.ext import *
import advisor as adv
import CONSTANTS


def start(update, context):
    # TODO: Add explaination of the bot
    str_val = "Welcome " + str(update.message.chat_id) + ', Lets start'
    update.message.reply_text(str_val)


def general(update, context):
    tickers = ["SPY", "QQQ", "IEI", "LQD", "TA35.TA", "FB", "GOOGL", 'AMAZ']  # The Name Tiker
    adv.calculate_protfolio(tickers, update.message.chat_id)
    context.bot.sendPhoto(chat_id=update.message.chat.id, photo=open(str(update.message.chat_id) + '.png', 'rb'))


def health_tech(update, context):
    tickers = ["COCP", "BLRX", "ADMP", "STIM", "TENX", "MTP", "VXRT", 'EDSA']  # The Name Tiker
    adv.calculate_protfolio(tickers, update.message.chat_id)
    context.bot.sendPhoto(chat_id=update.message.chat.id, photo=open(str(update.message.chat_id) + '.png', 'rb'))


def utils(update, context):
    tickers = ["ENIC", "AGR", "MDU", "HE", "CMSA", "AWR", "EDN", 'HNP']  # The Name Tiker
    adv.calculate_protfolio(tickers, update.message.chat_id)
    context.bot.sendPhoto(chat_id=update.message.chat.id, photo=open(str(update.message.chat_id) + '.png', 'rb'))


def energy_minerals(update, context):
    tickers = ["MTR", "BCEI", "CEIX", "INDO", "GBR", "PNRG", "ESTE", 'AR']  # The Name Tiker
    adv.calculate_protfolio(tickers, update.message.chat_id)
    context.bot.sendPhoto(chat_id=update.message.chat.id, photo=open(str(update.message.chat_id) + '.png', 'rb'))


def finance(update, context):
    tickers = ["VBFC", "XYF", "VINO", "TBBK", "VSPRU", "BRPAU", "ELVT", 'GMTX']  # The Name Tiker
    adv.calculate_protfolio(tickers, update.message.chat_id)
    context.bot.sendPhoto(chat_id=update.message.chat.id, photo=open(str(update.message.chat_id) + '.png', 'rb'))


def tech_services(update, context):
    tickers = ["JOBS", "CLST", "MOXC", "TKAT", "TZOO", "GB", 'TAOP']  # The Name Tiker
    adv.calculate_protfolio(tickers, update.message.chat_id)
    context.bot.sendPhoto(chat_id=update.message.chat.id, photo=open(str(update.message.chat_id) + '.png', 'rb'))


def main():
    print("Starting....")
    updater = Updater(CONSTANTS.API_KEY, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('general', general))
    dp.add_handler(CommandHandler('health', health_tech))
    dp.add_handler(CommandHandler('utils', utils))
    dp.add_handler(CommandHandler('energy', energy_minerals))
    dp.add_handler(CommandHandler('finance', finance))
    dp.add_handler(CommandHandler('tech_services', tech_services))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()