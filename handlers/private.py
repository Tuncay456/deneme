from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgIAAx0CUPE31gACHUZiiPmt4YAJ5GqvyJNZeDthLoZlVQACswsAAipQUUoso7YJ7GnT1h4E")
    await message.reply_text(
        f"""Ben **{bn}** !!
Reklam atmak için tasarlandım. Şuanda amatör bir yazılım olabilirim, olsun Sahime mesaj atabilirsiniz. Bilgi 
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💖 Asistan", url="https://t.me/movingmusic"

                    ),
                    InlineKeyboardButton(
                        "📣 Kanal", url="https://t.me/sohbetdestek"
                    ),                    
                    InlineKeyboardButton(
                        "🌀 Repo", url="https://github.com/Mehmetbaba06" 
                    ), 
                ]
            ]
        )
    )
