from django.apps import AppConfig


class NotesConfig(AppConfig):
    name = 'notes'
    def ready(self):
        # Now that the app is ready, let's set the signal handlers by importing the module
        from . import signals
