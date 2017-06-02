"""Discord bot."""

import shutil

import discord
from discord.ext import commands

from tools import make_embed_message

startup_extensions = ["automation"]


class AutomaBot(commands.Bot):
    """Discord bot specialization."""

    def __init__(self, get, update_channel, **options):
        """Init AutomaBot.

        :param get: The Queue reader side.
        :param update_channel: The notification channel id
        :param **options: Default commands.Bot parameters
        """
        super().__init__(**options)
        self.get = get
        self.update_channel = update_channel
        self.terminal_size = shutil.get_terminal_size((80, 20))[0]

    async def on_ready(self):
        """
        Override bot.on_ready function.

        When AutomaBot is ready, print its username
        in console and start notification process
        """
        self_username = self.user.name + "#" + self.user.discriminator
        self.load_extensions()
        print(f"""{f' Logged in as {self_username}': ^{self.terminal_size}}""")
        await self.notification_handler()

    async def on_command_error(self, exception, context):
        """
        Override bot.on_command_error function.

        Error handling function.
        """
        if isinstance(exception, discord.ext.commands.errors.CommandNotFound):
            msg = """Sorry, this command is unknown to me... :japanese_ogre:\
                    \nDo you need help? If so, just type \
                    ***!help*** :sunglasses:"""
        elif isinstance(exception,
                        discord.ext.commands.errors.DisabledCommand):
            msg = ":sleeping:"
        elif isinstance(exception,
                        discord.ext.commands.errors.CheckFailure):
            msg = """:octagonal_sign: you are not allowed to do this.\
                    \nOnly an :alien: can wake me up..."""
        elif isinstance(exception,
                        discord.ext.commands.errors.CommandInvokeError):
            msg = exception.original
            print(msg)
        else:
            msg = type(exception)
            print(msg)
        await self.send_message(context.message.channel, msg)

    def load_extensions(self):
        """
        Load extensions at startup.

        Credits go to @leovoel (https://github.com/leovoel). You can find
        this code here : https://gist.github.com/leovoel/46cd89ed6a8f41fd09c5
        """
        for extension in startup_extensions:
            try:
                self.load_extension(extension)
            except Exception as e:
                exc = '{}: {}'.format(type(e).__name__, e)
                print('Failed to load extension {}\n{}'.format(extension, exc))
        print(f"{f' Extensions loaded ': ^{self.terminal_size}}")

    async def notification_handler(self):
        """
        Send a message to a channel when datas are available.

        Datas are sent by the api when a light state changes.
        """
        print(f"{f' Fully functionnal ': ^{self.terminal_size}}")
        print(f"{f' Type Ctrl + C to close ': ^{self.terminal_size}}")
        print("\n\\" + "#" * (self.terminal_size-2) + "/")
        while not self.is_closed:
            data = await self.get()
            data["author"] = "AutomaBot"
            msg = make_embed_message(title="Update!", datas=data, bot=self)
            channel = self.get_channel(self.update_channel)
            await self.send_message(channel, embed=msg)