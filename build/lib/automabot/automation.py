"""Discord bot automation cog."""

import json

import aiohttp
from discord.ext import commands

from .bot import APIconnectionError
from .tools import load_params, make_embed_message


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
            msg = """You must specify a command. \
                    \nType **!help light** for more.:bulb: """
            await self.bot.send_message(ctx.message.channel, msg)

    @light.command(name='get', pass_context=True)
    async def get(self, ctx, lamp=None):
        """
        Return lamps status.

        If lamp is given, return lamp status.
        Contact the api to get light status and writes it as a list
        """
        tmp = await self.bot.send_message(ctx.message.channel, "Requesting")
        r = ""

        url = self.url_get
        if lamp is not None:
            url += "?lamp=" + lamp

        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as resp:
                    r = await resp.text()
        except aiohttp.errors.ClientOSError:
            raise APIconnectionError()

        datas = json.loads(r)
        if lamp is not None:
            datas = {lamp: datas}

        embed = make_embed_message("**Lights states**", datas,
                                   self.bot, ctx.message)
        await self.bot.edit_message(tmp, new_content='Right now : ',
                                    embed=embed)

    @light.command(name='set', pass_context=True)
    async def set(self, ctx, lamp, state):
        """
        Set lamp state.

        Changes state of [lamp] to [state] and sends server response
        """
        tmp = await self.bot.send_message(ctx.message.channel, "Requesting")
        payload = {'lamp': lamp, 'state': state, 'user_agent': 'AutomaBot'}
        r = ""

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(self.url_post, data=payload) as resp:
                    r = await resp.text()
        except aiohttp.errors.ClientOSError:
            raise APIconnectionError()

        embed = make_embed_message("*Result!*", json.loads(r), self.bot,
                                   ctx.message)
        await self.bot.edit_message(tmp, new_content='Right now : ',
                                    embed=embed)


def setup(bot):
    """Use this class as cog when using extension autoloader."""
    bot.add_cog(Automation("config.json", bot))
