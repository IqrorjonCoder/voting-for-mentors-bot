from telegram.ext import Updater, MessageHandler, CommandHandler, ConversationHandler, Filters, CallbackQueryHandler
import buttons
import voting_for_mentors


def start(update, context):
    update.message.reply_text("*Salom! Astrumning mentorlari uchun baho bering!*", parse_mode="Markdown",
                              reply_markup=buttons.voting_button)


def code_runner():
    updater = Updater(token="5784773177:AAFlBQWWOSyUA3IRLgyGgEf_duZwo1Huc4U")
    dispacher = updater.dispatcher

    dispacher.add_handler(CommandHandler('start', start))

    dispacher.add_handler(ConversationHandler(
        entry_points=[MessageHandler(Filters.regex("🎲 Ovoz berish"), voting_for_mentors.start_voting)],
        states={
            1: [CallbackQueryHandler(voting_for_mentors.select_group)],
            2: [CallbackQueryHandler(voting_for_mentors.select_mentor)],
            3: [CallbackQueryHandler(voting_for_mentors.select_result)],
            4: [CallbackQueryHandler(voting_for_mentors.select_becauseof)],
            5: [CallbackQueryHandler(voting_for_mentors.submit)],
        },
        fallbacks=[CommandHandler('stop', start)]
    ))


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    code_runner()
