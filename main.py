import logging
import urllib.request, urllib.parse, urllib.error

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

# Use this to log messages
LOGGER = logging.getLogger(__name__)

# to encode URL
def urlencode(qp):
    return urllib.parse.urlencode(qp)

class StartpageExtension(Extension):

    def __init__(self):
        super(StartpageExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())

class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = list()

        if event.get_argument():
            LOGGER.info('Showing Startpage search for "{}"'.format(
                event.get_argument()))
            items.append(ExtensionResultItem(
                icon='images/icon.svg',
                name='Search on Startpage',
                description='Search for "{}".'.format(event.get_argument()),
                on_enter=OpenUrlAction(
                    'https://www.startpage.com/do/dsearch?{}'.format(
                        urlencode({'query': event.get_argument()})
                    ))
            )
            )

        return RenderResultListAction(items)

if __name__ == '__main__':
    StartpageExtension().run()
