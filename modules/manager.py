from logger import logger
from utils import menu_message

from .database import Database
from .mint import Mint


class Manager:
    @staticmethod
    async def menu() -> None:
        menu_message()
        module_num = input("Module number: ")
        if module_num == "1":
            Database.create_database()
        elif module_num == "2":
            await Mint.mint_mode()
        else:
            logger.error("[MANAGER] Wrong module selected")
