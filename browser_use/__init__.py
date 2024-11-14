from browser_use.logging_config import setup_logging

setup_logging()
from browser_use.agent.service import Agent as Agent
from browser_use.browser.service import BrowserService as Browser
from browser_use.controller.service import ControllerService as Controller
from browser_use.dom.service import DomService

__all__ = ['Agent', 'Browser', 'Controller', 'DomService']
