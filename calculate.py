async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text

    try:
        value = eval(msg)
        await update.message.reply_text(f'{msg} = {value}')
    except:
        await update.message.reply_text('Не могу посчитать такое, попробуй что-то еще: ')