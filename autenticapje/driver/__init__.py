"""Gerenciador do webdriver para a execução dos bots."""

from __future__ import annotations

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager

from .constants import WORKDIR as WORKDIR
from .constants.webdriver import (
    ARGUMENTS,
    PREFERENCES,
    SETTINGS,
)
from .web_element import WebElementBot


class BotDriver:
    """Gerenciador do webdriver para a execução dos bots."""

    def __init__(self) -> None:
        """Inicialize o driver do bot com as configurações do sistema."""
        options = Options()

        for argument in ARGUMENTS:
            options.add_argument(argument)

        preferences = PREFERENCES
        preferences.update({
            "printing.print_preview_sticky_settings.appState": SETTINGS,
        })

        options.add_experimental_option("prefs", preferences)

        cache_manager = DriverCacheManager()
        driver_manager = ChromeDriverManager(
            cache_manager=cache_manager,
        )
        service = Service(executable_path=driver_manager.install())
        self.driver = Chrome(options=options, service=service)

        webelement = WebElementBot.set_driver(self.driver)

        self.driver._web_element_cls = webelement
        self.wait = WebDriverWait(self.driver, 30)
