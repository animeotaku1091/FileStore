#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
         text = f"<b>○ ᴏᴡɴᴇʀ : <a href='tg://user?id={OWNER_ID}'>ŦrαfͥαlͣgͫαrŁαw</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/animeotaku109'>ᴀɴɪᴍᴇ ᴏᴛᴀᴋᴜ </a>\n○ ᴀɴɪᴍᴇ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/teamotaku109'>ᴛᴇᴀᴍ ᴏᴛᴀᴋᴜ</a>\n○ ᴏɴɢᴏɪɴɢ ᴀɴɪᴍᴇ : <a href='https://t.me/ongoingotaku109'>ᴏɴɢᴏɪɴɢ ᴏᴛᴀᴋᴜ</a>\n○ ᴀɴɪᴍᴇ ᴄʜᴀᴛ : <a href='https://t.me/animeotakugc109'>ᴏᴛᴀᴋᴜ ᴄʜᴀᴛ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('🍁 ᴘʀᴇᴍɪᴜᴍ', url='https://t.me/LUFFY1JOYBOY')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
