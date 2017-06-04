"""Main program.

This file is based on @Greut (https://github.com/greut) 's main file
in his TravisBot project (https://github.com/greut/travisbot)
"""

import asyncio
import logging
import shutil

import discord
from discord.ext import commands
from pyfiglet import Figlet

from bot import AutomaBot
from tools import load_params
from web import make_app


def is_owner(ctx):
    """Check owner."""
    if isinstance(ctx.message.channel, discord.PrivateChannel):
        # Yes, I keep a "backdoor" in the bot
        author = ctx.message.author
        return author.name + "#" + author.discriminator == "Maël Pedretti#1416"
    return ctx.message.channel.server.owner == ctx.message.author


async def main(token, queue, channel, prefix, desc):
    """Run main program."""
    bot = AutomaBot(get=queue, update_channel=channel,
                    command_prefix=prefix,
                    description=desc, self_bot=False)

    @bot.command(pass_context=True)
    @commands.check(is_owner)
    async def sleep(ctx):
        await bot.change_presence(status=discord.Status.dnd, afk=True)
        msg = 'Going to sleep. See you :wave:'
        for comm in bot.commands:
            if comm is not "wakeup":
                bot.commands[comm].enabled = False
        await bot.say(msg)

    @bot.command(pass_context=True, hidden=True)
    @commands.check(is_owner)
    async def wakeup(ctx):
        for comm in bot.commands:
            if comm is not "wakeup":
                bot.commands[comm].enabled = True
        await bot.change_presence(status=discord.Status.online, afk=False)
        msg = 'Goooooooooood morniiing vietnammmmmm :bomb:'
        await bot.say(msg)

    await bot.start(token)


if __name__ == "__main__":
    """Catch main function."""

    params = load_params(param="bot")

    HOST = params['HOST']
    PORT = params['PORT']
    token = params['token']
    channel = params['update_channel_id']
    prefix = params['bot_command_prefix']
    desc = params['bot_description']

    debug = False

    queue = asyncio.Queue()

    app = make_app(queue.put)

    loop = asyncio.get_event_loop()
    if debug:
        loop.set_debug(True)
        logging.getLogger('asyncio').setLevel(logging.DEBUG)

    handler = app.make_handler()
    loop.run_until_complete(app.startup())

    server = loop.create_server(handler, host=HOST, port=PORT)
    try:
        srv = loop.run_until_complete(server)
        terminal_width = shutil.get_terminal_size((80, 20))[0]
        TOPBAR = f"/{'#' * (terminal_width - 2)}\\\n"
        print(TOPBAR)
        print(Figlet(font='banner').renderText('  AUTOMABOT'))
        print("\\" + "#" * (terminal_width-2) + "/")
        print(TOPBAR)
        print(f"{f' Listening on: {HOST}:{PORT} ': ^{terminal_width}}")
        loop.run_until_complete(main(token, queue.get, channel, prefix, desc))
    except KeyboardInterrupt:
        pass

    srv.close()
    loop.close()
