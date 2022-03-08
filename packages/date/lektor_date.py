from datetime import datetime, date
from zoneinfo import ZoneInfo
from lektor.pluginsystem import Plugin

class DatePlugin(Plugin):
    name = u'Lektor Date plugin'
    description = 'Add date objects to your jinja templates.'
    
    def on_setup_env(self, **extra):
        self.env.jinja_env.globals.update(
            date=date, datetime=datetime,
            ZoneInfo=ZoneInfo,
        )
