from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`as-salamu'alaikum wr. wb.`π")


@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`as-salamu'alaikum wr. wb.`π")


@register(outgoing=True, pattern='^.L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`wa'alaikumussalam wr. wb.`π")


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`wa'alaikumussalam wr. wb.`π")


CMD_HELP.update({
    "salam":
    "β PΚα΄Ι’ΙͺΙ΄ : Assalamu'alaikum wr. wb.\
\n\nβ‘πΎππΏβ‘: `.P`\
\nβ³ : Untuk Memberi Salam.\
\n\nβ‘πΎππΏβ‘: `.L`\
\nβ³ : Untuk Menjawab Salam."
})
