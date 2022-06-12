from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import ReplyKeyboardMarkup

buttons = ReplyKeyboardMarkup([['help']])

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'salom, qandaysiz {update.effective_user.first_name}',),
    update.message.reply_text('✋',)

def hi(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('✋',),
    update.message.reply_text('👋',),
    update.message.reply_text('🤙',),
    update.message.reply_text('🤚',),

def good(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('👍',),

def bye(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('👋',),
    update.message.reply_text('🖖',),

def kiss(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('💋',),
    update.message.reply_text('😙',),
    update.message.reply_text('😽',),
    update.message.reply_text('😗',),
    update.message.reply_text('😘',),
    update.message.reply_text('😚',)

def one(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('1️⃣',),

def two(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('2️⃣',),

def three(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('3️⃣',),

def four(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('4️⃣',),

def five(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('5️⃣',),

def six(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('6️⃣',),

def seven(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('7️⃣',),

def eight(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('8️⃣',),

def ten(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('🔟',),

def nine(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('9️⃣',),

def human(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('🧑',),

def please(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('🙏',),
    update.message.reply_text('🥺',),

def edit(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('📝',),

def pen(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('✍️',),

def pencil(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('📝',),

def Akobir(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('Akobir aka mening egam bo`ladi.U odam juda yaxshi va dasturlashni sevuvchi insondir, men u odamni xurmat qilaman ',),

def Muslima(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('Muslima Akobir akamning singlisi u uncha yaxshi qiz emasu lekin akam uni yaxshi ko`radi.Uko`pincha akam yo`g`ida mendan xar-hil vidyolar ko`radi bu esa menga yoqmaydi.',)

def hello1(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('✋',),
    update.message.reply_text('👋',)

def love(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('❤️',),
    update.message.reply_text('💛',),
    update.message.reply_text('🖤',),
    update.message.reply_text('💚',),
    update.message.reply_text('💙',),
    update.message.reply_text('💜',),
    update.message.reply_text('🧡',)

def salom(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('Iltimos Inglizchada so`zlashing',),
    update.message.reply_text('🙏',),

def dead(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('☠️',),
    update.message.reply_text('⚰️',),
    update.message.reply_text('💀',),

def phone(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('☎️',),

def bot(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('🤖',),

def fuck(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('🖕',),
    update.message.reply_text('😡',),
    update.message.reply_text('🤬',),

#def (update: Update, context: CallbackContext) -> 1:
#    update.message.reply_text('',),

#def (update: Update, context: CallbackContext) -> 1:
#    update.message.reply_text('',),

#def (update: Update, context: CallbackContext) -> 1:
#    update.message.reply_text('',),

#def (update: Update, context: CallbackContext) -> 1:
#    update.message.reply_text('',),

#def (update: Update, context: CallbackContext) -> 1:
#    update.message.reply_text('',),

def computer(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('💻',),
    update.message.reply_text('⌨️',)

def help(update: Update, context: CallbackContext) -> 1:
    update.message.reply_text('Sizda xatolar kuzatilgan bo`lsa uzur so`raymiz murojan uchun @Akobir9755 ga murojat qiling',),

updater = Updater('')#Bu yerga sizning API ingizni yozasiz

updater.dispatcher.add_handler(CommandHandler('start', hello))
updater.dispatcher.add_handler(CommandHandler('hi', hi))
updater.dispatcher.add_handler(CommandHandler('good', good))
updater.dispatcher.add_handler(CommandHandler('bye', bye))
updater.dispatcher.add_handler(CommandHandler('kiss', kiss))
updater.dispatcher.add_handler(CommandHandler('bye', bye))
updater.dispatcher.add_handler(CommandHandler('one', one))
updater.dispatcher.add_handler(CommandHandler('two', two))
updater.dispatcher.add_handler(CommandHandler('three', three))
updater.dispatcher.add_handler(CommandHandler('four', four))
updater.dispatcher.add_handler(CommandHandler('five', five))
updater.dispatcher.add_handler(CommandHandler('six', six))
updater.dispatcher.add_handler(CommandHandler('seven', seven))
updater.dispatcher.add_handler(CommandHandler('eight', eight))
updater.dispatcher.add_handler(CommandHandler('nine', nine))
updater.dispatcher.add_handler(CommandHandler('ten', ten))
updater.dispatcher.add_handler(CommandHandler('hello', hello1))
updater.dispatcher.add_handler(CommandHandler('salom', salom))
updater.dispatcher.add_handler(CommandHandler('hi', hello1))
updater.dispatcher.add_handler(CommandHandler('human', human))
updater.dispatcher.add_handler(CommandHandler('please', please))
updater.dispatcher.add_handler(CommandHandler('edit', edit))
updater.dispatcher.add_handler(CommandHandler('Akobir', Akobir))
updater.dispatcher.add_handler(CommandHandler('Muslima', Muslima))
updater.dispatcher.add_handler(CommandHandler('love', love))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('dead', dead))
updater.dispatcher.add_handler(CommandHandler('phone', phone))
updater.dispatcher.add_handler(CommandHandler('computer', computer))
updater.dispatcher.add_handler(CommandHandler('pencil', pencil))
updater.dispatcher.add_handler(CommandHandler('pen', pen))
updater.dispatcher.add_handler(CommandHandler('bot', bot))
updater.dispatcher.add_handler(CommandHandler('man', human))
updater.dispatcher.add_handler(CommandHandler('fuck', fuck))
#updater.dispatcher.add_handler(CommandHandler('', ))
#updater.dispatcher.add_handler(CommandHandler('', ))
#updater.dispatcher.add_handler(CommandHandler('', ))
#updater.dispatcher.add_handler(CommandHandler('', ))
#updater.dispatcher.add_handler(CommandHandler('', ))
#updater.dispatcher.add_handler(CommandHandler('', ))

updater.start_polling()
updater.idle()
