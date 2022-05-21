from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# Maho tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_sticker( 
                "CAACAgIAAx0CUPE31gACHUZiiPmt4YAJ5GqvyJNZeDthLoZlVQACswsAAipQUUoso7YJ7GnT1h4E",
                caption=(f"""**Merhaba {message.from_user.mention}  👍\nBen {bot}!\nTelegram Grupları İçin Özel Hazırlandım.n\Sahibim ile iletişime geçiniz.**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Grubuna Ekle ❱ ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🚀 Reklam", url="https://t.me/Taliamusicasistant"
                    ),
                    InlineKeyboardButton(
                        "📣 Kanalım", url="https://t.me/Sohbetdestek"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🙄 Yardım", url="https://t.me/Botdestekgrubu" 
                    ),
                    InlineKeyboardButton(
                        "Repo 🇹🇷", url=f"https://t.me/Mahoaga"
                    )
                ]
                
           ]
        ),
    )
 
