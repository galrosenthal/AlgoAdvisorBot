from telegram.ext import *
import advisor as adv
import CONSTANTS


def start(update, context):
    str_val = "Welcome " + str(update.message.chat_id) + ', Lets start'
    update.message.reply_text(str_val)


def general(update, context):
    general_tickers = ["SPY", "QQQ", "IEI", "LQD", "TA35.TA", "FB", "GOOGL", 'AMAZ']  # The Name Tiker

    adv.calculate_protfolio(general_tickers, update.message.chat_id)

    context.bot.sendPhoto(chat_id=update.message.chat.id, photo=open(str(update.message.chat_id) + '.png', 'rb'))


def main():
    print("Starting....")
    updater = Updater(CONSTANTS.API_KEY, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('general', general))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()