import logging

from telethon import events, __version__
from ChannelAutoPost import *
from telethon import events, Button
from sys import argv
from ChannelAutoPost.plugins import *

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


@ChannelAutoPost.on(events.NewMessage(pattern="^/start$"))
async def start(event):
    await event.reply(
        f"Hello! I am a **Channel Auto Post bot**, I can help you manage your channel efficiently. You need to deploy your own instance for that from the source given below! :)", 
        buttons=[
            [   Button.url("Team SL Bots🇱🇰", "https://t.me/SlBots_Admins"),
                Button.url("Join Our Channel", "https://telegram.me/SLBotOfficial"),
            ],
            [
                Button.url("Source", "https://github.com/DARKEMPIRELS/ChannelAutoPost"),
                Button.url("Developer", "https://telegram.me/ImDark_Empire"),                
            ]
        ], 
    )


@ChannelAutoPost.on(events.NewMessage(pattern="^/help$"))
async def help(event):
    await event.reply("These are the things I can do,\n\n"
                      "> Forward posts of one or more channels to provided channel!\n"
                      "> Add custom footer at last of all new posts\n"
                      "> Remove all of the new media post caption as per user's choice\n"
                      "> Can be used as an userbot, therefore you just need to join the channels from where to leech and "
                      "need not to be admin in them, you just need to admin in the forwarding or `TO_CHANNEL` channel!"
                      "\n\n**NOTE:** You have to add the bot in both the channels from where to forward and to where forward! (For bot instances and not userbots)"
                      "\n\nLiked the bot? Give the [repo](github.com/DARKEMPIRESL/ChannelAutoPost) a star! With ❤️ by @ImDark_Empire",
                      link_preview=False,
                     )


@ChannelAutoPostUB.on(events.NewMessage(pattern="^.alive$", outgoing=True))
async def alive_ub(event):
    await event.edit("Sup? I am alive :)")
    
    
@ChannelAutoPost.on(events.NewMessage(pattern="^/alive$", func=lambda e: e.is_private, from_users=Config.OWNER_ID))
async def alive_bot(event):
    await event.reply("Sup? I am alive :)")
    
    
if __name__ == "__main__":
    ChannelAutoPost.start(bot_token=Config.BOT_TOKEN)
    log.info("Bot Successfully Started....")
    if Config.USE_AS_USERBOT:
        log.info("Starting Your Userbot... Kindly Wait")
        if not Config.SESSION:
            log.error("SESSION is missing... Bot is quitting. Kindly fill all the required vars to get it started!")
            quit(1)
        ChannelAutoPostUB.start()        
    if len(argv) not in (1, 3, 4):
        ChannelAutoPost.disconnect()
    else:
        log.info("--------------------------------------")
        log.info("|> Channel AutoPost Bot By @ImDark_Empire <|")
        log.info("--------------------------------------")
        log.info("Tele Version: " + __version__)        
        log.info("You bot is now running, Do {}alive to confirm!".format("." if Config.USE_AS_USERBOT else "/"))
        ChannelAutoPost.run_until_disconnected()    
