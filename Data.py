from idbot import app
from Config import Config
from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = "Hey {}. \n\nWelcome to JNS Family 🎊🎉 \n\nUsing this bot you can check id of any group, user, bot, channel and even stickers."

    if Config.OWNER_ID != 0:
        if Config.OWNER_NAME:
            START += (
                f"\n\n**My Owner :-** [{Config.OWNER_NAME}](tg://user?id={Config.OWNER_ID}) \n@JNS_BOTS🎊"
            )
        else:
            print(
                "You added OWNER_ID but not OWNER_NAME. You need to put both or neithers"
            )
            print("Quitting the bot")
            raise SystemExit
    else:
        START += f"\n\nBy @JNS_BOTS ♥"
    START += "\n\n~ Your ID is `{}`"

    # About Message
    ABOUT = "**🔖About This Bot🔖** \n\n👩‍💻 𝐃𝐄𝐕 : 🕵️ JINTONS \n\n💡 𝐂𝐑𝐄𝐃𝐈𝐓𝐒 : Everyone in this journey\n\n🧰𝗙𝗿𝗮𝗺𝗲𝘄𝗼𝗿𝗸 : [Pyrogram](docs.pyrogram.org) \n\n💻 𝐋𝐀𝐍𝐆𝐔𝐀𝐆𝐄 : [Python](www.python.org) \n\n🏷️ 𝐁𝐎𝐓 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 : [ＪƝ⟆ ᗷ〇Ƭ⟆](https://t.me/jns_bots)"

    if Config.OWNER_ID != 0:
        if Config.OWNER_NAME:
            ABOUT += (
                f"\n\nMy Owner :- [{Config.OWNER_NAME}](tg://user?id={Config.OWNER_ID})"
            )
        else:
            print(
                "You added OWNER_ID but not OWNER_NAME. You need to put both or neither"
            )
            print("Quitting the bot")
            raise SystemExit

    # Help Message
    HELP = "**Help & Features** \n\n1) Send any message to get your ID. \n2) Forward any message from any user/bot/channel or anonymous admins to get ID. \n3) Send any sticker to get sticker id. \n4) Use Inline Mode to send your ID in any chat. \n5) Add in group / channel to get ID. \n6) Use /id command: \n- in private: To get ID through username \n- in group/channel: To get ID of that chat. \n\nBy @MysteryBots ♥"

    # Deploy Message
    DEPLOY = '**Wanna create your own such bot??** \n\nThis is simple and open source bot. \nJust click below on source code and tap on "Deploy to Heroku" to create your own bot. \n\nClick Here for [Source Code](https://github.com/MysteryBots/ID-Bot)'

    # Home Button
    home_button = [[InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")]]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✌ How to Use ✌", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about"),
        ],
        [InlineKeyboardButton("Create your own bot", callback_data="deploy")],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/MysteryBots")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/MysteryBotsChat")],
    ]
