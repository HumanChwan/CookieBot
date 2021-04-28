import datetime
from typing import List

import discord
import dataService.data_service as dt_srv
from data.guild_show import GuildPretty
from data.member_show import MemberPretty
from MathCookie import random_between
import asyncio
from data.emoji import Emoji

month_finder = (
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
)

spank_list = (
    'https://media1.tenor.com/images/ef5f040254c2fbf91232088b91fe2341/tenor.gif?itemid=13569259',
    'https://media1.tenor.com/images/d0f32f61c2964999b344c6846b30e1d6/tenor.gif?itemid=13665166',
    'https://media1.tenor.com/images/19e30607441c8a08330d91329fd18e69/tenor.gif?itemid=7922491',
    'https://media1.tenor.com/images/6b3dda2e995a02ad50ae788a16bfbd64/tenor.gif?itemid=12325914',
    'https://media1.tenor.com/images/2eb222b142f24be14ea2da5c84a92b08/tenor.gif?itemid=15905904'
)

kill_list = (
    'https://media1.tenor.com/images/0917e9f68e7d277135a9f885f953888b/tenor.gif?itemid=17763115',
    'https://media1.tenor.com/images/bb4b7a7559c709ffa26c5301150e07e4/tenor.gif?itemid=9955653',
    'https://media1.tenor.com/images/a05561ce485557e5eec86a7ac7f141e9/tenor.gif?itemid=18467587',
    'https://media1.tenor.com/images/a80b2bf31635899ac0900ea6281a41f6/tenor.gif?itemid=5535365',
    'https://media1.tenor.com/images/eb7fc71c616347e556ab2b4c813700d1/tenor.gif?itemid=5840101'
)

kick_list = (
    'https://media1.tenor.com/images/fb2a19c9b689123e6254ad9ac6719e96/tenor.gif?itemid=4922649',
    'https://media1.tenor.com/images/ea2c3b49edf2080e0ef2a2325ddb4381/tenor.gif?itemid=14835708',
    'https://media1.tenor.com/images/4dd99934237218f35c02b7cbf4ac9f9f/tenor.gif?itemid=16580938',
    'https://media1.tenor.com/images/7ad8cdd67a2937de54a75e7858f430c6/tenor.gif?itemid=19326658',
    'https://media1.tenor.com/images/2ce5a017f6556ff103bce87b273b89b7/tenor.gif?itemid=16407803'
)

slap_list = (
    'https://media1.tenor.com/images/612e257ab87f30568a9449998d978a22/tenor.gif?itemid=16057834',
    'https://media1.tenor.com/images/477821d58203a6786abea01d8cf1030e/tenor.gif?itemid=7958720',
    'https://media1.tenor.com/images/9ea4fb41d066737c0e3f2d626c13f230/tenor.gif?itemid=7355956',
    'https://media1.tenor.com/images/fb17a25b86d80e55ceb5153f08e79385/tenor.gif?itemid=7919028',
    'https://media1.tenor.com/images/1ba1ea1786f0b03912b1c9138dac707c/tenor.gif?itemid=5738394'
)

punch_list = (
    'https://media1.tenor.com/images/31686440e805309d34e94219e4bedac1/tenor.gif?itemid=4790446',
    'https://media1.tenor.com/images/2487a7679b3d7d23cadcd51381635467/tenor.gif?itemid=11451829',
    'https://media1.tenor.com/images/ee3f2a6939a68df9563a7374f131fd96/tenor.gif?itemid=14210784',
    'https://media1.tenor.com/images/a7a67336a11b60d292179be1246240c9/tenor.gif?itemid=17175633',
    'https://media1.tenor.com/images/d7c30e46a937aaade4d7bc20eb09339b/tenor.gif?itemid=12003970'
)

kiss_list = (
    'https://media1.tenor.com/images/7fd98defeb5fd901afe6ace0dffce96e/tenor.gif?itemid=9670722',
    'https://media1.tenor.com/images/ea9a07318bd8400fbfbd658e9f5ecd5d/tenor.gif?itemid=12612515',
    'https://media1.tenor.com/images/78095c007974aceb72b91aeb7ee54a71/tenor.gif?itemid=5095865',
    'https://media1.tenor.com/images/bc5e143ab33084961904240f431ca0b1/tenor.gif?itemid=9838409',
    'https://media1.tenor.com/images/558f63303a303abfdddaa71dc7b3d6ae/tenor.gif?itemid=12879850'
)

lewd_list = (
    'https://media1.tenor.com/images/e848ab2fd27bef61e0b81db32bd38763/tenor.gif?itemid=17512632',
    'https://media1.tenor.com/images/b46b4c6e802545843696e664901f36be/tenor.gif?itemid=20655343',
    'https://media1.tenor.com/images/73eaea88d9b2f191bbed563192d7efb1/tenor.gif?itemid=14588244',
    'https://media1.tenor.com/images/9d921ae2f69420beb68dcf083d7e0f43/tenor.gif?itemid=14913237',
    'https://media1.tenor.com/images/b3c78661c57ce895b827d7424425953d/tenor.gif?itemid=15104649',
    'https://media1.tenor.com/images/ee25cfc39c61a1b1478dcfe72e7116e0/tenor.gif?itemid=16442725'
)


def help_cool_game():
    return 'Upon initiating the game you would be asked to set some characteristics.',\
           'After Setting of characteristics, you would asked to enter a Number(Four-Digit).',\
            'The entered number would be processed as a guess.',\
            'After Processing \'Correct Digits\' and \'Correct Places\' would displayed ' +\
            'which represent the correct digits and correct Places of the digits ' +\
            'wrt to the random system generated number.',\
            'Following the end of maximum guesses or by guessing the Correct the number, game will end. :thumbsup:'\
            'Time Out for entering the number is set at 5 minutes after which game will terminate automatically.',\
            'Entering EndGame will terminate the game in between the game.',


async def embed_help(channel):
    embed_boi = discord.Embed(title="Command/Help",
                              description="Shows the Commands and General over-through of the Bot")
    embed_boi.add_field(name='ck CoolGame', value='ck CoolGame help\n ck CoolGame init\n ck CoolGame Terminate')
    embed_boi.add_field(name='ck math <expression>',
                        value='\nCan Solve Math expressions : presently +, -, *, /, ^ are supported.')

    await channel.send(content=None, embed=embed_boi)


async def embed_help_cool_game(channel):
    embed_boi = discord.Embed(title='CoolGame Cmds and Help', description='CoolGame Commands')

    help_cool = help_cool_game()

    i = 1
    for Instruction in help_cool:
        embed_boi.add_field(name=str(i) + '. :cookie:', value=Instruction, inline=False)
        i += 1

    embed_boi.add_field(name='_ _', value='_ _', inline=False)
    embed_boi.add_field(name='HAVE FUN!', value='_ _', inline=False)

    await channel.send(content=None, embed=embed_boi)


async def cookie_quote(channel):
    one = asyncio.create_task(channel.send('**Dood cookie? cookie what?** Now take this, idc'))
    two = asyncio.create_task(channel.send(':cookie:'))
    await one
    await two


async def game_terminate(message_meta):
    await message_meta.channel.send(f':cookie: **{message_meta.author.name} |** Game terminated :frowning:')


async def guild_join_message(guild):
    channel_id = dt_srv.find_welcome_channel_id(guild.id)

    if not channel_id:
        return

    channel = guild.get_channel(channel_id)
    await channel.send('Hi! Yo doods')


async def wrong_input(message_meta: discord.message):
    await message_meta.channel.send(f':cookie: **{message_meta.author.name} |**' +
                                    ' Wrong Input Style :frowning:')


async def incorrect_expression(message_meta: discord.message):
    await message_meta.channel.send(f':cookie: **{message_meta.author.name} |**' +
                                    ' Incorrect expression? At least get your shit right man :pensive:')


async def correct_expression(answer: int, message_meta: discord.message):
    await message_meta.channel.send(f':cookie: **{message_meta.author.name} |** Nice there you go,' +
                               f' Your expression yieldeth : **{answer}**')


async def parallel_init_error(message_meta: discord.message):
    await message_meta.channel.send(f':cookie: **{message_meta.author.name} |**' +
                                    ' Already initiated! UwU :smile:')


async def init_successful(message_meta: discord.message):
    embed_one = discord.Embed(title='Game has Initialised', description=f'Player: <@{message_meta.author.id}>')
    embed_one.add_field(name='Tries : ', value='10', inline=False)
    embed_one.set_image(url='https://github.com/HumanChwan/CookieBot/blob/master/Cool_Game.png?raw=true')

    await message_meta.channel.send(content=None, embed=embed_one)


async def empty_terminate_error(message_meta: discord.message):
    await message_meta.channel.send(f':cookie: **{message_meta.author.name} |**' +
                               ' Lol! what do you wanna terminate? _B A K A_ :nerd:')


async def terminate_successful(message_meta: discord.message):
    await message_meta.channel.send(f':cookie: **{message_meta.author.name} |**' +
                                    ' Game terminated _sad moment_ :disappointed:')


async def repeat_input(message_meta: discord.message):
    await message_meta.channel.send(f':cookie: **{message_meta.author.name} |**' +
                                    ' Found Repeated Digits _sad moment_ :expressionless:')


async def publish_result(message_meta: discord.message, partial_result, tries_left: int):
    embed_one = discord.Embed(title='Guess Results', description=f'Player: <@{message_meta.author.id}>')
    embed_one.add_field(name='Correct Digits:', value=str(partial_result[0]))
    embed_one.add_field(name='Correct Places:', value=str(partial_result[1]))
    embed_one.add_field(name='Tries Left:', value=str(tries_left))
    if partial_result[1] == 4:
        embed_one.add_field(name='Guessed the Correct Number :tada: :confetti_ball:', value='_ _')

    await message_meta.channel.send(content=None, embed=embed_one)


async def ran_out_of_tries(message_meta: discord.message, param):
    embed_one = discord.Embed(title='Ran Out Of Tries :disappointed:',
                              description=f'Player: <@{message_meta.author.id}>')
    embed_one.add_field(name='Better Luck Next Time :thumbsup:', value='_ _', inline=False)
    embed_one.add_field(name='The Random number was :', value=param[0]+param[1]+param[2]+param[3])

    await message_meta.channel.send(content=None, embed=embed_one)


async def present_guild_data(author: discord.member,
                             guild_data: GuildPretty, guild_discord: discord.guild, channel: discord.channel):
    embed_boi = discord.Embed(title=':cookie: **Cookie Stats**', description='_ _')
    embed_boi.set_thumbnail(url=
                    'https://github.com/HumanChwan/CookieBot/blob/master/Cookie_Monster.png?raw=true')
    embed_boi.set_author(name=author.name, icon_url=author.avatar_url)
    # embed ------> guild_discord.name
    if guild_data.cool_game_data['One'][1]:
        one = guild_data.cool_game_data['One']
        member = guild_discord.get_member(one[1])
        display_name = member.nick
        if not display_name:
            display_name = member.name
        leaderboard = f'**1.** __**{display_name}**__ : **{one[0]}** :first_place:\n'
        # embed ----- > guild_discord.get_member(guild_data.cool_game_data['One'][1])
    else:
        leaderboard = f'**1.** ------- : ---- :first_place:\n'

    if guild_data.cool_game_data['Two'][1]:
        two = guild_data.cool_game_data['Two']
        member = guild_discord.get_member(two[1])
        display_name = member.nick
        if not display_name:
            display_name = member.name
        leaderboard += f'**2.** __**{display_name}**__ : **{two[0]}** :second_place:\n'
        # embed ----- > guild_discord.get_member(guild_data.cool_game_data['One'][1])
    else:
        leaderboard += f'**2.** ------- : ---- :second_place:\n'
        # embed ---- > empty

    if guild_data.cool_game_data['Three'][1]:
        three = guild_data.cool_game_data['Three']
        member = guild_discord.get_member(three[1])
        leaderboard += f'**3.** __**{member.display_name}**__ : **{three[0]} :third_place:**\n'
        # embed ----- > guild_discord.get_member(guild_data.cool_game_data['One'][1])
    else:
        leaderboard += f'**3.** ------- : ---- :third_place:\n'
        # embed ---- > empty

    embed_boi.add_field(name=f'__Leaderboard of {guild_discord.name}__', value=leaderboard, inline=False)
    # embed ----> guild.discord.member_count
    embed_boi.add_field(name='Member Count:', value=str(guild_discord.member_count))

    embed_boi.set_footer(text=f'Server ID: {guild_discord.id}')
    # mbed.footer -----> guild_discord.id
    await channel.send(content=None, embed=embed_boi)


async def emoji_try(content, emojis, channel: discord.channel):
    for emote in emojis:
        if content == ':' + emote.name + ':':
            if emote.animated:
                await channel.send(f'<a:{emote.name}:{emote.id}>')
            else:
                await channel.send(f'<:{emote.name}:{emote.id}>')
            break


async def profile_picture(to_be_presented: discord.member, author: discord.member, channel: discord.channel):
    embed_make = discord.Embed(title=f'Avatar : {to_be_presented.display_name}', description='_ _')
    embed_make.set_author(name=author.name, icon_url=author.avatar_url)
    embed_make.set_image(url=to_be_presented.avatar_url)

    await channel.send(content=None, embed=embed_make)


async def present_member_data(author: discord.member, mention_name: str,
                              member_show: MemberPretty, member_show_join: datetime.datetime,
                              channel: discord.channel):
    embed_boi = discord.Embed(title=':cookie: **Profile Stats**', description='_ _')
    embed_boi.set_thumbnail(url=
                    'https://github.com/HumanChwan/CookieBot/blob/master/Cookie_Monster.png?raw=true')
    embed_boi.set_author(name=author.name, icon_url=author.avatar_url)

    embed_boi.add_field(name=f'__**CoolGame Stats: {mention_name}**__ ', value='_ _', inline=False)
    embed_boi.add_field(name=f' 1. Rank               : {member_show.rank}', value='_ _', inline=False)
    embed_boi.add_field(name=f' 2. Total Games Played : {member_show.total_played}', value='_ _', inline=False)
    embed_boi.add_field(name=f' 3. Total Games Won    : {member_show.total_won}', value='_ _', inline=False)
    embed_boi.add_field(name='_ _', value='_ _', inline=False)

    date = str(member_show_join.day) + ' ' + month_finder[member_show_join.month-1] + ', ' + str(member_show_join.year)
    embed_boi.add_field(name=f'**Joined the Server on :** __{date}__', value='_ _', inline=False)

    await channel.send(content=None, embed=embed_boi)


def spank(self: bool, victim: str, bad_boi: int):
    if self:
        message_displayed = 'Congratulations, You have ~~played~~ spanked yourself :flushed:'
    else:
        message_displayed = ':flushed: :flushed: :flushed: nyaaaaa~~!!' \
                            f' {victim} just got spanked by {bad_boi}'
    ind = random_between(0, len(spank_list)-1)
    url_spank = spank_list[ind]

    return message_displayed, url_spank


def kill(self: bool, victim: str, bad_boi: int):
    if self:
        message_displayed = 'F, why so sad man, take puchi <3'
    else:
        message_displayed = f'kekek, DIEEEE!!!!! :ghost:, {victim} got killed by {bad_boi}'
    ind = random_between(0, len(kill_list) - 1)
    url_kill = kill_list[ind]

    return message_displayed, url_kill


def kick(self: bool, victim: str, bad_boi: int):
    if self:
        message_displayed = 'Hehe, true you do deserved to be kicked, slimey-simp :smiling_imp:'
    else:
        message_displayed = f'Yes, {victim} get kicked like a good boi, nice kogeki {bad_boi}-chan!!'
    ind = random_between(0, len(kick_list) - 1)
    url_kick = kick_list[ind]

    return message_displayed, url_kick


def punch(self: bool, victim: str, bad_boi: int):
    if self:
        message_displayed = ':( why slap yourself man, are you sad? (P.S. : You still gonna be slapped :smile:)'
    else:
        message_displayed = f'kuso gaki {victim} got punched by {bad_boi}-kun!!'
    ind = random_between(0, len(punch_list) - 1)
    url_punch = punch_list[ind]

    return message_displayed, url_punch


def slap(self: bool, victim: str, bad_boi: int):
    if self:
        message_displayed = 'YESSSS!!! Harder!!! ~~nyaaa!!!'
    else:
        message_displayed = f'{victim} got slapped by {bad_boi}!! LOL'
    ind = random_between(0, len(slap_list) - 1)
    url_slap = slap_list[ind]

    return message_displayed, url_slap


def kiss(self: bool, victim: str, bad_boi: int):
    if self:
        message_displayed = 'Bruh, lol respect o7 pretty self-sufficient :thumbsup:'
    else:
        message_displayed = f'{victim} got kissed by {bad_boi}, kyaaaa!!.... ok :/'
    ind = random_between(0, len(kiss_list) - 1)
    url_kiss = kiss_list[ind]

    return message_displayed, url_kiss


def lewd(self: bool, victim: str, bad_boi: int):
    if self:
        message_displayed = 'bruhhhhhh noicee :o :shrug1:'
    else:
        message_displayed = f'lewd lewd everywhere :pensive: horny mfs {victim} and {bad_boi}'
    ind = random_between(0, len(lewd_list) - 1)
    url_lewd = lewd_list[ind]

    return message_displayed, url_lewd


action = (
    spank,
    kill,
    kick,
    slap,
    punch,
    kiss,
    lewd
)


async def perform_action_embed(author: discord.member, mentions, channel: discord.channel,
                               command: str):
    cmd_coefficient = 0
    if command == 'spank':
        cmd_coefficient = 1
    elif command == 'kill':
        cmd_coefficient = 2
    elif command == 'kick':
        cmd_coefficient = 3
    elif command == 'slap':
        cmd_coefficient = 4
    elif command == 'punch':
        cmd_coefficient = 5
    elif command == 'kiss':
        cmd_coefficient = 6
    elif command == 'lewd':
        cmd_coefficient = 7

    to_be_victimised = author
    if mentions:
        to_be_victimised = mentions[0]

    self = to_be_victimised == author

    get_data = action[cmd_coefficient-1](self, to_be_victimised.name, author.name)

    embed_boi = discord.Embed(title=command.upper()+'!!', description='**'+get_data[0]+'**')
    embed_boi.set_author(name=author.name, icon_url=author.avatar_url)
    embed_boi.set_image(url=get_data[1])

    await channel.send(content=None, embed=embed_boi)


def animated(if_ani: bool) -> str:
    if if_ani:
        return 'a'
    else:
        return ''


async def try_formatted_interpreter(content: str, channel: discord.channel, display_name: str):
    line_content = content.split('\n')

    found = False
    send_string = ''
    for string in line_content:
        list_content = string.split()
        for i in range(len(list_content)):
            if list_content[i][0] == list_content[i][-1] == ':':
                emote = dt_srv.get_emote(list_content[i].replace(':', ''), channel.guild.id)
                if not emote:
                    continue
                found = True
                list_content[i] = f'<{animated(emote.animated)}:{emote.name}:{emote._id}>'
        send_string += ' '.join(list_content) + '\n'
    if found:
        await channel.send(send_string)


def obtain_pg_number(footer: str):
    footer = footer.replace('Page ', '')
    pg = ''
    for i in footer:
        if i == '/':
            break
        pg += i

    return int(pg)


async def emoji_cheat_sheet(author, page_change: int, message_meta: discord.message):
    total_pages = (dt_srv.cnt_emote() + 9)//10
    if total_pages == 0:
        total_pages = 1

    if page_change == 0:
        page_number = 1
    else:
        page_number = obtain_pg_number(message_meta.embeds[0].footer.text)
        page_number += page_change
        if page_number < 1 or page_number > total_pages:
            return

    if page_change == 0:
        embed_emote = discord.Embed(title='Emojis', description='_ _')
        embed_emote.set_author(name=author.name, icon_url=author.avatar_url)
        embed_emote.set_footer(text=f'Page {page_number}/{total_pages}')
        embed_emote.set_thumbnail(url=
                                'https://github.com/HumanChwan/CookieBot/blob/master/Cookie_Monster.png?raw=true')

        emotes = dt_srv.get_emotes(0, 10)
        ind = 1
        for emote in emotes:
            embed_emote.add_field(name=f'**{ind}.** <{animated(emote.animated)}:{emote.name}:{emote._id}>',
                                  value=f'**:{emote.name}:** | ID : {emote._id}', inline=False)
            ind += 1
        message = await message_meta.channel.send(content=None, embed=embed_emote)
        # message = await message_meta.channel.fetch_message(id=message_meta.channel.last_message_id)
        emote_1 = asyncio.create_task(message.add_reaction(emoji='⬅'))
        emote_2 = asyncio.create_task(message.add_reaction(emoji='➡'))
        await emote_1
        await emote_2
    else:
        embed_emote = message_meta.embeds[0]
        embed_emote.clear_fields()
        embed_emote.set_footer(text=f'Page {page_number}/{total_pages}')
        emotes = dt_srv.get_emotes((page_number - 1) * 10, page_number * 10)
        ind = (page_number - 1) * 10 + 1
        for emote in emotes:
            # __:{emote.name}:__ ({emote._id}) :
            embed_emote.add_field(name=f'**{ind}.** <{animated(emote.animated)}:{emote.name}:{emote._id}>',
                                  value=f'**:{emote.name}:** | ID : {emote._id}', inline=False)
            ind += 1

        await message_meta.edit(content=None, embed=embed_emote)


async def uwu(channel: discord.channel):
    await channel.send('⢐⢕⢕⢕⢕⢕⣕⢕⢕⠕⠁⢕⢕⢕⢕⢕⢕⢕⢕⠅⡄⢕⢕⢕⢕⢕⢕⢕⢕⢕\n' +
                    '⢕⢕⢕⢕⢕⠅⢗⢕⠕⣠⠄⣗⢕⢕⠕⢕⢕⢕⠕⢠⣿⠐⢕⢕⢕⠑⢕⢕⠵⢕\n' +
                    '⢕⢕⢕⢕⠁⢜⠕⢁⣴⣿⡇⢓⢕⢵⢐⢕⢕⠕⢁⣾⢿⣧⠑⢕⢕⠄⢑⢕⠅⢕\n' +
                    '⢕⢕⠵⢁⠔⢁⣤⣤⣶⣶⣶⡐⣕⢽⠐⢕⠕⣡⣾⣶⣶⣶⣤⡁⢓⢕⠄⢑⢅⢑\n' +
                    '⠍⣧⠄⣶⣾⣿⣿⣿⣿⣿⣿⣷⣔⢕⢄⢡⣾⣿⣿⣿⣿⣿⣿⣿⣦⡑⢕⢤⠱⢐\n' +
                    '⢠⢕⠅⣾⣿⠋⢿⣿⣿⣿⠉⣿⣿⣷⣦⣶⣽⣿⣿⠈⣿⣿⣿⣿⠏⢹⣷⣷⡅⢐\n' +
                    '⣔⢕⢥⢻⣿⡀⠈⠛⠛⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⡀⠈⠛⠛⠁⠄⣼⣿⣿⡇⢔\n' +
                    '⢕⢕⢽⢸⢟⢟⢖⢖⢤⣶⡟⢻⣿⡿⠻⣿⣿⡟⢀⣿⣦⢤⢤⢔⢞⢿⢿⣿⠁⢕\n' +
                    '⢕⢕⠅⣐⢕⢕⢕⢕⢕⣿⣿⡄⠛⢀⣦⠈⠛⢁⣼⣿⢗⢕⢕⢕⢕⢕⢕⡏⣘⢕\n' +
                    '⢕⢕⠅⢓⣕⣕⣕⣕⣵⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣷⣕⢕⢕⢕⢕⡵⢀⢕⢕\n' +
                    '⢑⢕⠃⡈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢃⢕⢕⢕\n' +
                    '⣆⢕⠄⢱⣄⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢁⢕⢕⠕⢁\n' +
                    '⣿⣦⡀⣿⣿⣷⣶⣬⣍⣛⣛⣛⡛⠿⠿⠿⠛⠛⢛⣛⣉⣭⣤⣂⢜⠕⢑⣡⣴⣿')
