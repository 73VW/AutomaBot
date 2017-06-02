"""Discord bot automation cog."""

import json

import aiohttp
from discord.ext import commands

from tools import load_params, make_embed_message


class Automation:
    """Class used in AutomaBot to make everything related to automation."""

    def __init__(self, filename, bot):
        """Init Automation class.

        :param filename: file containing automation config.
        :param bot: instance of class AutomaBot.
        :attr url_get: Url used to get light states.
        :attr url_post: Url used to set light states.
        """
        self.filename = filename
        self.bot = bot
        params = load_params(param="automation")
        self.url_get = params['url_get']
        self.url_post = params['url_post']

    @commands.group(pass_context=True)
    async def light(self, ctx):
        """Everything that is light related."""
        if len(ctx.message.content.split(" ")) is 1:
            msg = "You must specify a command. \
                    Type **!help light** for more."
            await self.bot.send_message(ctx.message.channel, msg)

    @light.command(name='get', pass_context=True)
    async def get(self, ctx):
        """
        Return lights status.

        Contact the api to get light status and writes it as a list
        """
        tmp = await self.bot.send_message(ctx.message.channel, "Requesting")

        async with aiohttp.ClientSession() as session:
            async with session.get(self.url_get) as resp:
                r = await resp.text()

        embed = make_embed_message("**Lights states**", json.loads(r),
                                   self.bot, ctx.message)
        await self.bot.edit_message(tmp, new_content='Right now : ',
                                    embed=embed)

    @light.command(name='set', pass_context=True)
    async def set(self, ctx, lamp, state):
        """
        Set lamp state.

        Changes state of lamp to state (both contained in lamp_and_state and
        sending server response
        TODO: improve this function to detect api errors.
        TODO: improve this function to send async http requests
        """
        tmp = await self.bot.send_message(ctx.message.channel, "Requesting")
        if lamp is not None and state is not None:
            payload = {'lamp': lamp, 'state': state, 'user_agent': 'AutomaBot'}

            async with aiohttp.ClientSession() as session:
                async with session.post(self.url_post, data=payload) as resp:
                    r = await resp.text()

            embed = make_embed_message("*Result!*", json.loads(r), self.bot,
                                       ctx.message)
            await self.bot.edit_message(tmp, new_content='Right now : ',
                                        embed=embed)
        else:
            msg = """You forgot parameters...
                    Do you ride bikes with no wheels?... use *!help light* for
                    help """
            await self.bot.edit_message(tmp, msg)


def setup(bot):
    """Use this class as cog when using extension autoloader."""
    bot.add_cog(Automation("config.json", bot))
