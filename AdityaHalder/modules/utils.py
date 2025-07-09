import asyncio

from .vars import Config
from math import ceil
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton
from typing import Union, List
from youtubesearchpython import VideosSearch


PREFIXES = Config.COMMAND_PREFIXES
HANDLERS = Config.COMMAND_HANDLERS


def commandx(commands: Union[str, List[str]]):
    return filters.command(commands, PREFIXES)


def commandz(commands: Union[str, List[str]]):
    return filters.command(commands, HANDLERS)


def get_youtube_video(query: str):
    try:
        find = VideosSearch(query, limit=1).result()
        data = find["result"][0]
        ytlink = data["link"]
        return [ytlink]
    except Exception as e:
        print(e)
        return 0


class EqInlineKeyboardButton(InlineKeyboardButton):
    def __eq__(self, other):
        return self.text == other.text

    def __lt__(self, other):
        return self.text < other.text

    def __gt__(self, other):
        return self.text > other.text


def paginate_plugins(page_n, plugin_dict, prefix, chat=None):
    from .. import app
    if not chat:
        plugins = sorted(
            [
                EqInlineKeyboardButton(
                    x.__NAME__,
                    callback_data="{}_plugin({})".format(
                        prefix, x.__NAME__.lower()
                    ),
                )
                for x in plugin_dict.values()
            ]
        )
    else:
        plugins = sorted(
            [
                EqInlineKeyboardButton(
                    x.__NAME__,
                    callback_data="{}_plugin({},{})".format(
                        prefix, chat, x.__NAME__.lower()
                    ),
                )
                for x in plugin_dict.values()
            ]
        )

    pairs = list(zip(plugins[::3], plugins[1::3], plugins[2::3]))
    i = 0
    for m in pairs:
        for _ in m:
            i += 1
    if len(plugins) - i == 1:
        pairs.append((plugins[-1],))
    elif len(plugins) - i == 2:
        pairs.append(
            (
                plugins[-2],
                plugins[-1],
            )
        )

    COLUMN_SIZE = 3

    max_num_pages = ceil(len(pairs) / COLUMN_SIZE)
    modulo_page = page_n % max_num_pages

    if len(pairs) > COLUMN_SIZE:
        pairs = pairs[
            modulo_page * COLUMN_SIZE: COLUMN_SIZE * (modulo_page + 1)
        ] + [
            (
                EqInlineKeyboardButton(
                    "❮",
                    callback_data="{}_prev({})".format(prefix, modulo_page),
                ),
                EqInlineKeyboardButton(
                    "Owner",
                    url=f"tg://openmessage?user_id={app.id}",
                ),
                EqInlineKeyboardButton(
                    "❯",
                    callback_data="{}_next({})".format(prefix, modulo_page),
                ),
            )
        ]

    return pairs
