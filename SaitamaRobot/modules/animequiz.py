import html
import random
import KarmaRobot.modules.animequiz_string as animequiz_string
from KarmaRobot import dispatcher
from telegram import ParseMode, Update, Bot
from KURUMIBOT.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@run_async
def aq(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(animequiz_string.Animequiz))

AQ_HANDLER = DisableAbleCommandHandler("aq", aq)

dispatcher.add_handler(AQ_HANDLER)
