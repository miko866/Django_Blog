from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # call constructor in to users
    def ready(self):
        import users.signals
