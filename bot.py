import logging

from aiogram import Bot, Dispatcher, executor, types

from chek_wiki import check_wiki

logging.basicConfig(level=logging.INFO)

token = '6167192201:AAHwYd-JhYJ16LRCNrACiuGw2lfajGX1cA4'

bot = Bot(token=token)

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_start(msg: types.Message):
    await msg.reply("Assalomu aleykum botga hush kelibsiz, bu bot wikipedia boti.")


@dp.message_handler(commands=['help'])
async def send_help(msg: types.Message):
    await msg.reply("Biror narsa haqida bilmoqchi bo'lsangiz yozing.")


@dp.message_handler()
async def send_help(msg: types.Message):
    data = check_wiki(msg.text)
    if data['data']:
        await msg.answer(data['summary'])
    elif data['word']:
        answer = ''
        for i in data['search']:
            answer += i
        await msg.answer(f"Siz qidirgan sozga malumot topilmadi.\nQuyidagi sozlardan birini qidirmadingizmi?\n{answer}")
    else:
        await msg.reply("Siz qidirgan sozga umuman malumot topilmadi")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
