from telegram.ext import ConversationHandler
import buttons
import to_sql

states = {
    "select_group": 1,
    "select_mentor": 2,
    "select_result": 3,
    "select_becauseof": 4,
    "submit": 5

}


def start_voting(update, context):
    update.message.reply_text("*Yonalishlardan birini tanlang !*", parse_mode="Markdown", reply_markup=buttons.groups)
    return states["select_group"]


def select_group(update, context):
    query = update.callback_query
    if query.data == "🔙 orqaga 🔙":
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        query.message.reply_text("*Salom! Astrumning mentorlari uchun baho bering!*", parse_mode="Markdown", reply_markup=buttons.voting_button)
        return ConversationHandler.END
    else:
        context.user_data['yonalish'] = query.data
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        query.message.reply_text("*Mantorlardan birini tanlang !*", parse_mode="Markdown",
                                 reply_markup=buttons.mentors[context.user_data['yonalish']])
        return states["select_mentor"]


def select_mentor(update, context):
    query = update.callback_query
    if query.data == "🔙 orqaga 🔙":
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        query.message.reply_text("*Yonalishlardan birini tanlang !*", parse_mode="Markdown", reply_markup=buttons.groups)
        return states["select_group"]
    else:
        context.user_data['mentor'] = query.data
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        query.message.reply_text("*Baho bering !*", parse_mode="Markdown", reply_markup=buttons.result)
        return states["select_result"]


def select_result(update, context):
    query = update.callback_query
    if query.data == "🔙 orqaga 🔙":
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        query.message.reply_text("*Mantorlardan birini tanlang !*", parse_mode="Markdown", reply_markup=buttons.mentors[context.user_data['yonalish']])
        return states["select_mentor"]
    else:
        context.user_data['result'] = query.data
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        query.message.reply_text("*Sababni kiriting !*", parse_mode="Markdown", reply_markup=buttons.because_of[context.user_data['result']])
        return states["select_becauseof"]


def select_becauseof(update, context):
    query = update.callback_query
    if query.data == "🔙 orqaga 🔙":
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        query.message.reply_text("*Baho bering !*", parse_mode="Markdown", reply_markup=buttons.result)
        return states["select_result"]
    else:
        context.user_data['becauseof'] = query.data
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        query.message.reply_text("*Tasdiqlang !*", parse_mode="Markdown", reply_markup=buttons.submit)
        return states["submit"]


def submit(update, context):
    query = update.callback_query
    if query.data == "tasdiqlandi":
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        query.message.reply_text(f"*Tasdiqlandi✅ \nAstrumning mentorlari uchun baho bering!*", parse_mode="Markdown", reply_markup=buttons.voting_button)
        to_sql.to_sql(context.user_data['mentor'], context.user_data['result'], context.user_data['becauseof'])
        to_sql.to_googlesheets(context.user_data['mentor'], context.user_data['result'], context.user_data['becauseof'])
        return ConversationHandler.END
    else:
        context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)
        query.message.reply_text("*Tasdiqlanmadi❌ \nAstrumning mentorlari uchun baho bering!*", parse_mode="Markdown", reply_markup=buttons.voting_button)
        return ConversationHandler.END