

import asyncio
import os

from telethon import __version__ 
from userbot import ALIVE_NAME, TG_CHANNEL, TG_GRUP
from userbot.thunderconfig import Config
from userbot.utils import lightning_cmd

ACE_ALV_IMG = os.environ.get("ACE_ALV_IMG", None)
if ACE_ALV_IMG is None:
    ALV_ACE = "https://telegra.ph/file/4fd9c80c16fd8b6683ba4.jpg"
else:
    ALV_ACE = ACE_ALV_IMG


version = "4.5"
python_version = "3.8.5"

# Functions
def lightning_Read_time(seconds: int) -> str:
    count = 0
    kirsh = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            lol_hehehe, result = divmod(seconds, 60)
        else:
            lol_hehehe, result = divmod(seconds, 24)
        if seconds == 0 and lol_hehehe == 0:
            break
        time_list.append(int(result))
        seconds = int(lol_hehehe)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        khan += time_list.pop() + ", "

    time_list.reverse()
    khan += ":".join(time_list)

    return khan

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "ace"

TG = str(TG_GRUP) if TG_GRUP else "Not  Yet😁😁"
TG_CHANN = str(TG_CHANNEL) if TG_CHANNEL else "Not Yet😁😁"


from userbot import CMD_LIST

Ace_cap = "**Ace 𝙸𝚂 `ɘᴎi|ᴎO`**\n\n"
Ace_cap += f"**†rïdεη† ﾚïgh†'š mαš†εr**          : {DEFAULTUSER}\n"
Ace_cap += f"⚔️⚔️ {DEFAULTUSER}'s⚔️⚔️ ɢʀօʊք   : {TG}\n"  
Ace_cap += f"⚔️⚔️{DEFAULTUSER}'s⚔️⚔️ ƈɦǟռռɛʟ : {TG_CHANN}\n\n"
Ace_cap += f"`тєℓєтнσи νєяѕισи`       : {__version__}\n"
Ace_cap += "`ρყƚԋσɳ ʋҽɾʂισɳ`           : 3.9.0\n\n"
Ace_cap += "`ֆʊքքօʀƭ ƈɦǟռռɛʟ`          : [ᴊᴏɪɴ](https://t.me/@ACE_BOT_ON)\n"
Ace_cap += "`ֆʊքքօʀƭ ɢʀօʊք`            : [ᴊᴏɪɴ](https://t.me/@ACE_BOT_SUPPORT_ON)\n"
Ace_cap += "`𝘾𝙊𝙋𝙔𝙍𝙄𝙂𝙃𝙏`:              [MOKIB](https://t.me//TURU_LOB_0)\n"


@borg.on(ACE_cmd(pattern=r"alive"))
@borg.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def ACE(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, ALV_LIGHTNING, caption=Ace_cap)
    await alive.delete()
