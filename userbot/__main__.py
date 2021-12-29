import os
import re
import sys
import asyncio 
os.system("pip install telethon==1.24.0")

import telethon.utils
from telethon import Button, TelegramClient, custom, events

from userbot import LOGS, LEGENDversion, bot
from userbot.Config import Config
from var import Var

from .start import abuses, addons, assistants, hekp, install, module, spams

l1 = Config.COMMAND_HAND_LER
l2 = Config.SUDO_COMMAND_HAND_LER
LEGEND_PIC = "https://telegra.ph/file/e753315316673cff51085.mp4"

perf = "[ †hê Lêɠêɳ̃dẞø† ]"

onbot = "start - Check if I am Alive \nhack - Hack Anyone Through String Session\nping - Pong! \ntr - <lang-code> \nbroadcast - Sends Message To all Users In Bot \nid - Shows ID of User And Media. \naddnote - Add Note \nnotes - Shows Notes \nspam - spam value text (value < 100)\nbigspam - spam value text (value > 100) \nraid - Raid value Reply to Anyone \nreplyraid - Reply To Anyone \ndreplyraid - Reply To Anyone \nrmnote - Remove Note \nalive - Am I Alive? \nbun - Works In Group , Bans A User. \nunbun - Unbans A User in Group \nprumote - Promotes A User \ndemute - Demotes A User \npin - Pins A Message \nstats - Shows Total Users In Bot \npurge - Reply It From The Message u Want to Delete (Your Bot Should be Admin to Execute It) \ndel - Reply a Message Tht Should Be Deleted (Your Bot Should be Admin to Execute It)"

bot_father = "@BotFather"

mybot = Config.BOT_USERNAME
if mybot.startswith("@"):
    botname = mybot
else:
    botname = f"@{mybot}"


async def add_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        print(f"LEGEND_STRING - {str(e)}")
        sys.exit()


if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Var.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
            ).start(bot_token=Var.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("♥️ Starting LegendBot ♥️")
            bot.loop.run_until_complete(add_bot(Config.BOT_USERNAME))
            LOGS.info("🥇🔥 LegendBot Startup Completed 🔥🥇")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

print("📍⚜Loading Modules / Plugins⚜✔")

tgbot = bot.tgbot


async def killer():
    LEGEND_USER = bot.me.first_name
    The_LegendBoy = bot.uid
    legd_mention = f"[{LEGEND_USER}](tg://user?id={The_LegendBoy})"
    name = f"{legd_mention}'s Assistant"
    description = (
        f"I am Assistant Of {legd_mention}.This Bot Can Help U To Chat With My Master"
    )
    starkbot = await tgbot.get_me()
    bot_id = starkbot.first_name
    if bot_id.endswith("Assistant"):
        print("Bot Starting")
    else:
        try:
            await bot.send_message("@BotFather", "/setinline")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", perf)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setcommands")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", onbot)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setname")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", name)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setdescription")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", description)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "/setuserpic")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_file(
                "@BotFather", "userbot/resources/pics/-4965507108355287505_121.jpg"
            )
        except Exception as e:
            print(e)
    # else:
    # print("Turn On ASSISTANT to Use This")


async def legends():
    LEGEND_USER = bot.me.first_name
    The_LegendBoy = bot.uid
    legd_mention = f"[{LEGEND_USER}](tg://user?id={The_LegendBoy})"
    yescaption = f"Hello Sir/Miss Something Happened \nDing Dong Ting Tong Ping Pong\nSuccessfully LegendBot Has Been Deployed \nMy Master ~ 『{legd_mention}』 \nVersion ~ {LEGENDversion}\nClick Below To Know More About Me👇🏾👇👇🏼"
    try:
        TRY = [[Button.inline("⭐ Start ⭐", data="start")]]
        await tgbot.send_file(
            bot.me.id, LEGEND_PIC, caption=yescaption, buttons=TRY, incoming=True
        )
    except:
        pass


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"start")))
async def help(event):
    await event.delete()
    if event.query.user_id is not bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message="Hello sir/miss,\nHow can i help u",
            buttons=[
                [
                    Button.url(" Support ", "https://t.me/Legend_Userbot"),
                    Button.url(" Updates ", "https://t.me/Official_LegendBot"),
                ],
                [custom.Button.inline("⚙ Sᴇᴛᴛɪɴɢs ⚙", data="osg")],
                [custom.Button.inline("⚜ Hack ⚜", data="hck")],
            ],
        )

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"osg")))
async def help(event):
    await event.delete()
    if event.query.user_id == bot.uid:
        await tgbot.send_message(
            event.chat_id,
            message=f"**Which type of setting do you want to edit?\nYou can change anything from these..!!\nAny kind for help do join [Lêɠêɳ̃dẞø†](t.me/Official_LegendBot)**",
            buttons=[
                [
                    Button.inline("Var Explain", data="var"),
                    Button.inline("All Var", data="allvar"),
                ],
                [Button.inline("Close", data="close")],
            ],
        )


@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"var")))
async def users(event):
    await event.delete()
    grabon = ".set var <varname> <value> ex:- .set var ALIVE_NAME LegendBoy \n\n To Know All Var Go Back And Click On All Var"
    await tgbot.send_message(event.chat_id, grabon)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"allvar")))
async def users(event):
    await event.delete()
    grabon = "All Var Name Are Given Below :\n\nABUSE = ON/ OFF\nALIVE_EMOJI = ANY EMOJI, Example: ✨\nALIVE_MESSAGE = Any Message ,Example : LegendBot Is Online\nALIVE_PIC = telegraph Link, use .tm to get it\nASSISTANT = ON / OFF\nAWAKE_PIC = telegraph link, get from .tm<reply to pic>\n"
    await tgbot.send_message(event.chat_id, grabon)



@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"hck")))
async def users(event):
    await event.delete()
    grabon = "I am Giving U Full Power To Hack Anyone Through String session\nClick Here 👉/hack."
    await tgbot.send_message(event.chat_id, grabon)


bot.loop.run_until_complete(killer())
bot.loop.run_until_complete(module())
bot.loop.run_until_complete(addons())
bot.loop.run_until_complete(abuses())
bot.loop.run_until_complete(assistants())
bot.loop.run_until_complete(spams())
bot.loop.create_task(hekp())
bot.loop.run_until_complete(install())

print(
    f"""
╔════❰LEGENDBOT❱═❍⊱❁۪۪
║┣⪼ OWNER - {Config.ALIVE_NAME}
║┣⪼ Group - @Legend_Userbot
║┣⪼ CREATOR - @The_LegendBoy
║┣⪼ LEGENDBOT - {LEGENDversion}
║┣⪼ ✨ 『🔱🇱 🇪 🇬 🇪 🇳 🇩 🔱』𝐔𝐬𝐞𝐫𝐛𝐨𝐭✨
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱"""
)
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

bot.loop.run_until_complete(legends())


if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()
