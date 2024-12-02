import importlib

from telegram import Update
<<<<<<< HEAD
from telegram.ext import (
    Application,
    ChatMemberHandler,
    CommandHandler,
    MessageHandler,
    MessageReactionHandler,
    filters,
)
=======
from telegram.ext import Application
>>>>>>> origin/master

from krddevbot import settings
from krddevbot.application import KrdDevBotApplication
from krddevbot.logging import init_logging
from krddevbot.request import HTTPXRequestWithRetry
<<<<<<< HEAD
from krddevbot.messages import track_user_messages
from krddevbot.commands import ping_command, help_command, list_command, rules_command
=======
>>>>>>> origin/master


if __name__ == "__main__":
    init_logging()
    application = Application.builder()\
        .application_class(KrdDevBotApplication)\
        .token(settings.BOT_TOKEN)\
        .request(HTTPXRequestWithRetry())\
        .get_updates_request(HTTPXRequestWithRetry())\
        .build()

<<<<<<< HEAD
    application.add_handler(CommandHandler("ping", ping_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("list", list_command))
    application.add_handler(CommandHandler("rules", rules_command))
    application.add_handler(ChatMemberHandler(greet_chat_members, ChatMemberHandler.CHAT_MEMBER))
    application.add_handler(MessageReactionHandler(antispam_reactions_checking))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, track_user_messages))
=======
    for app_name in settings.APPS:
        pkg = importlib.import_module('.'.join(('krddevbot', app_name)))
        pkg.init(application)
>>>>>>> origin/master

    application.run_polling(allowed_updates=Update.ALL_TYPES)
