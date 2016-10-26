from django.apps import AppConfig


class AsyncConfig(AppConfig):
    # we inherit from app config to override the ready() method
    name = 'async'
    verbose_name = "Async"

    # needed to register the django signals
    def ready(self):
        # needed to prevent models be loaded before app is in ready state
        from async.signals import register_signals
        register_signals()
