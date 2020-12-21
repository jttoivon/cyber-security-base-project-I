from django.apps import AppConfig

# https://docs.djangoproject.com/en/3.1/ref/applications/
class NotesConfig(AppConfig):
    name = 'notes'
    def ready(self):
        # Now that the app is ready, let's set the signal handlers by importing the signals module
        #from . import signals
        pass
