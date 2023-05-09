from aiogram.types import BotCommand

from lexicon.lexicon import LEXICON_COMMAND


async def main_menu_btn(bot):
    main_menu_command = [BotCommand(command=command, description=description)
                         for command, description in LEXICON_COMMAND.items()]

    await bot.set_my_commands(main_menu_command)