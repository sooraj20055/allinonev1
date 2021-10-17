#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @SpEcHIDe

from pyrogram import Client, __version__

from . import API_HASH, APP_ID, LOGGER, BOT_TOKEN 

from .User import User

class DonLee_Robot(Client):
    USER: User = None
    USER_ID: int = None

    def __init__(self):
        super().__init__(
            "DonLee_Robot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "DonLee_Robot/Modules"
            },
            workers=400,
            bot_token=BOT_TOKEN,
            sleep_threshold=10
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        bot_details = await self.get_me()
        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"@{bot_details.username}  സ്റ്റാർട്ട് ആയി 😃! "
        )
        self.USER, self.USER_ID = await User().start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("ഞാൻ സ്റ്റോപ് ആയി 😭")
