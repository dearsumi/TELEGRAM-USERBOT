from math import ceil
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton
from typing import Union, List

from .vars import Config

PREFIXES = Config.COMMAND_PREFIXES
HANDLERS = Config.COMMAND_HANDLERS


def commandx(commands: Union[str, List[str]]):
    return filters.command(commands, PREFIXES)


def commandz(commands: Union[str, List[str]]):
    return filters.command(commands, HANDLERS)


class EqInlineKeyboardButton(InlineKeyboardButton):
    def __eq__(self, other):
        return self.text == other.text

    def __lt__(self, other):
        return self.text < other.text

    def __gt__(self, other):
        return self.text > other.text


def paginate_plugins(page_n, plugin_dict, prefix, chat=None):
    from .. import app

    plugins = sorted(
        [
            EqInlineKeyboardButton(
                x.__NAME__,
                callback_data=(
                    f"{prefix}_plugin({x.__NAME__.lower()})"
                    if not chat
                    else f"{prefix}_plugin({chat},{x.__NAME__.lower()})"
                ),
            )
            for x in plugin_dict.values()
        ]
    )

    pairs = list(zip(plugins[::3], plugins[1::3], plugins[2::3]))
    remaining = len(plugins) - len(pairs) * 3
    if remaining == 1:
        pairs.append((plugins[-1],))
    elif remaining == 2:
        pairs.append((plugins[-2], plugins[-1]))

    COLUMN_SIZE = 3
    max_pages = ceil(len(pairs) / COLUMN_SIZE)
    page = page_n % max_pages if max_pages else 0

    if len(pairs) > COLUMN_SIZE:
        pairs = pairs[page * COLUMN_SIZE : (page + 1) * COLUMN_SIZE]
        pairs.append((
            EqInlineKeyboardButton("❮", callback_data=f"{prefix}_prev({page})"),
            EqInlineKeyboardButton("Owner", url=f"tg://openmessage?user_id={app.id}"),
            EqInlineKeyboardButton("❯", callback_data=f"{prefix}_next({page})"),
        ))

    return pairs
