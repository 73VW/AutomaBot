"""Discord bot."""

import shutil

import discord
from discord.ext import commands

from .tools import make_embed_message

startup_extensions = ["automabot.automation"]


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
        self.terminal_width = shutil.get_terminal_size((80, 20))[0]

    async def on_ready(self):
        """
        Override bot.on_ready function.

        When AutomaBot is ready, print its username
        in console and start notification process
        """
        self_username = self.user.name + "#" + self.user.discriminator
        self.load_extensions()
        print(f"{f' Logged in as {self_username}': ^{self.terminal_width}}")
        await self.notification_handler()

    async def on_command_error(self, exception, context):
        """
        Override bot.on_command_error function.

        Error handling function.
        """
        if isinstance(exception, discord.ext.commands.errors.CommandNotFound):
            msg = """Sorry, this command is unknown to me... :japanese_ogre:\
                    \nDo you need help? \
                    \nIf so, just type ***!help*** :sunglasses:"""
        elif isinstance(exception,
                        discord.ext.commands.errors.DisabledCommand):
            msg = ":sleeping:"
        elif isinstance(exception,
                        discord.ext.commands.errors.CheckFailure):
            msg = """:octagonal_sign: you are not allowed to do this.\
                    \nOnly an :alien: can wake me up..."""
        elif isinstance(exception,
                        discord.ext.commands.errors.MissingRequiredArgument):
            msg = """:thought_balloon: You forgot parameters.\
                    \nType !help [command] to get help :interrobang:"""
        elif isinstance(exception,
                        APIconnectionError):
            msg = """It seems we can't contact the API...:frowning2: \
            \nTake a rest and retry later.:play_pause: """
        elif isinstance(exception,
                        discord.ext.commands.errors.CommandInvokeError):
            msg = "oups... " + str(exception)
            print(msg)
        else:
            msg = "oups inconnu... " + str(type(exception)) + str(exception)
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
                exc = f'{type(e).__name__}: {e}'
                print(f'Failed to load extension {extension}\n{exc}')
        print(f"{' Extensions loaded ': ^{self.terminal_width}}")

    async def notification_handler(self):
        """
        Send a message to a channel when datas are available.

        Datas are sent by the api when a light state changes.
        """
        print(f"{' Fully functionnal ': ^{self.terminal_width}}")
        print(f"{' Type Ctrl + C to close ': ^{self.terminal_width}}")
        print("\n\\" + "#" * (self.terminal_width-2) + "/")
        while not self.is_closed:
            data = await self.get()
            data["author"] = "AutomaBot"
            msg = make_embed_message(title="Update!", datas=data, bot=self)
            channel = self.get_channel(self.update_channel)
            await self.send_message(channel, embed=msg)


class APIconnectionError(discord.ext.commands.errors.CommandError):
    """Exception raised when automation can't connect to client."""

    pass
