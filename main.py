import random
from aiogram import Bot, Dispatcher, executor, types
from rich.console import Console
from asyncio import sleep

console = Console()

API_TOKEN = console.input('[red]API TOKEN: ')
delay = int(console.input('[white]Delay Reply: '))
hello = console.input('[whute]Welcome Text: ')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

file = open('words.txt', 'r')
text = file.read().split('\n')
file.close()

@dp.message_handler(commands=['start', 'help'])
async def Start_Bot(message: types.Message):
    await message.reply(hello)

@dp.message_handler()
async def Trolling(message: types.Message):
      await sleep(delay)
      await message.answer(random.choice(text))
      console.log(f'{message.text}')
    
if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
