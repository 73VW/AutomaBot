"""Discord bot tools."""

import datetime
import os.path

import discord
import toml


states = "Off", "On"

default_config_fname = "default_config.toml"
config_fname = "config.toml"


def my_setup():
    """
    Set up bot parameters.

    Loads default config file with fields description and asks user for
    parameters.
    """
    new_params = {}
    params = load_params(fname=default_config_fname)
    sep = 8 * " " + 8 * "*" + 8 * " "

    print(sep + "You will now have to set parameters used by the bot.\n" +
          sep + "    Default values are printed between brackets.\n" +
          sep + "    Leave blank if you want to use default value")

    for param in params:
        new_params[param] = {}
        values = params[param]['value']
        descriptions = params[param]['description']
        for value in values:
            new_params[param][value] = ""
            if not values[value]:
                input_msg = f"{descriptions[value]} : "
            else:
                input_msg = f"{descriptions[value]} [{values[value]}] : "
            while not new_params[param][value]:
                input_var = input(input_msg)
                if not input_var:
                    new_params[param][value] = values[value]
                else:
                    new_params[param][value] = input_var
    print(new_params)
    with open(config_fname, 'w', encoding='utf-8') as fp:
        toml.dump(new_params, fp)
    return new_params


def load_params(fname=config_fname, param=""):
    """
    Load parameters from file.

    If config file doesn't exist, we ask user to build one
    """
    params = {}
    if not os.path.isfile(fname):
        params = my_setup()

    if not params:
        with open(fname, 'r', encoding='utf-8') as fp:
            params.update(toml.load(fp))

    if param:
        return params[param]
    else:
        return params


def make_embed_message(title, datas, bot, message=None):
    """
    Return an embed message for discord.

    Datas must be a simple dict
    """
    # embed properties
    embed_title = title
    embed_colour = discord.Colour(0x3c6d46)
    embed_timestamp = datetime.datetime.utcnow()
    embed = discord.Embed(title=embed_title, colour=embed_colour,
                          timestamp=embed_timestamp)

    # author properties
    if message is not None:
        author = message.author.name
        url = message.author.avatar_url
    else:
        author = datas.pop("author")
        url = bot.user.avatar_url

    author_name = author
    author_icon_url = url
    embed.set_author(name=author_name, icon_url=author_icon_url)

    # footer properties
    footer_text = bot.user.name
    footer_icon_url = bot.user.avatar_url
    embed.set_footer(text=footer_text, icon_url=footer_icon_url)

    # content
    inline = False
    for key, data in datas.items():
        if isinstance(data, bool):
            data = states[data]
        embed.add_field(name=key.title(), value=data, inline=inline)

    return embed
