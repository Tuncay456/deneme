from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only
from config import SUDO_USERS 

@Client.on_message(filters.group & filters.command(["katil", "asistan"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Beni Önce Yönetici Yapmalısın</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "Reklamcı"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"Senin İsteğin Üzerine Geldim")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Asistan Zaten Grupta Var</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🔵 Zaman Aşımı Hatası 🔵\n User {user.first_name} userbot için yoğun katılma istekleri nedeniyle grubunuza katılamadı! Asistanın grupta yasaklanmadığından emin olun."
            "\n\n Yada Asistan Hesabını Gruba Kendin Ekle </b>",
        )
        return
    await message.reply_text(
            "<b>Reklamcı Zaten Grupta Var</b>",
        )
    
@USER.on_message(filters.group & filters.command(["ayril", "asistanby"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>Kullanıcı grubunuzdan ayrılamadı!."
            "\n\nYada Kendin Çıkarabilirsin</b>",
        )
        return
 
@USER.on_message(filters.group & filters.command(["userbotleave"]))
@authorized_users_only
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>User couldn't leave your group! May be floodwaits."
            "\n\nOr manually kick me from to your Group</b>",
        )
        return


@Client.on_message(filters.command(["devil"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left = 0
        failed = 0
        lol = await message.reply("Aşkım ben tüm Gruplardan ayrılıyorum...")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left + 1
                await lol.edit(
                    f"Ayrılıyorum... Left: {left} chats. Failed: {failed} chats."
                )
            except:
                failed = failed + 1
                await lol.edit(
                    f"Ayrılıyorum... Left: {left} chats. Failed: {failed} chats."
                )
            await asyncio.sleep(0.7)
        await client.send_message(
            message.chat.id, f"Left {left} chats. Failed {failed} chats."
        )
 
 
