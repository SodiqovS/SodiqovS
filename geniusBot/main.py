import logging
from aiogram import Bot, Dispatcher, types, executor
from SearchMusic import searchmus
from tarjima_qil import tarjimasi

TOKEN = "1992139152:AAGKNnwp55Rn7NFmenB0CP9pN7Wzl9lUf9s"
logging.basicConfig(level=logging.INFO)

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)
kanal_ssilka = 'https://t.me/joinchat/LGK4ve2Vs0o2ZDZi'

@dp.message_handler(commands = "start")
async def start(message: types.Message):
    await message.answer("Salom\n🎶🎵Botga xush kelibsiz. Botni ishlatish qoidalarini bilish uhun /help ni kiriting")

@dp.message_handler(commands = "help")
async def start(message: types.Message):
    await message.answer("✅Botni ishlatish uchun unga artist nomi va qo'shiq nomini quyidagicha kiritng: \n\t\t \bArtistnomi , qo'shiq nomi\b ")

@dp.message_handler()
async def emojiText(message: types.Message):
    msg = message.text
    print(msg)
    try:
        at = msg.split(',')
        artist = at[0] 
        title = at[1]  
        
        answ = searchmus(artist,title)
        uzunlik = len(answ)
        if uzunlik >4096:
            answ1 = answ[:4093] + '...'
            answ2 = answ[4097:uzunlik] 

            await message.reply(answ1)
            await message.reply(answ2)
            try:
                await message.reply(tarjimasi(answ1))
                await message.reply(tarjimasi(answ2+f'\n©️ Kanalimiz 👇👇👇👇 \n{kanal_ssilka}'))
            except:
                pass
        else:
            await message.reply(answ+f'\nKanalimiz 👇👇👇👇 \n{kanal_ssilka}')
            if answ != "❗️So'rovda xatolik!! Bunday artist va qo'shiq nomini topolmadim.\nIltimos tekshirib qaytadan kiriting\n":
                await message.reply(tarjimasi(answ))
    
    except:
        await message.reply("❌Noto'g'ri format, qaytadan urining.\nBot ishlashi haqida ma'lumot olish uchun /help ni bosing")


    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)