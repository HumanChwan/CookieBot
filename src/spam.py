import discord
rimuru_spam_on = False


async def spam_boi(message_meta: discord.message,
                   victim: int, start_signal: str, stop_signal: str, client: discord.Client):
    global rimuru_spam_on
    found = False
    # SPAM MOMENT OREKI

    if not rimuru_spam_on and message_meta.content == start_signal:
        rimuru_spam_on = True
        member_to_spammed = message_meta.author

        for guild in client.guilds:
            for member in guild.members:

                if not found and member.id == victim:
                    member_to_spammed = member
                    found = True
                    break
            if found:
                break

        await member_to_spammed.create_dm()
        while rimuru_spam_on:
            await member_to_spammed.dm_channel.send(
                'lol get spammed\n'
                + 'lol get spammed\n'
                + 'lol get spammed\n'
                + 'lol get spammed\n'
            )
        return

    if message_meta.content == stop_signal:
        rimuru_spam_on = False
