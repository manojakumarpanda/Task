from django.apps import AppConfig


class UserAccountsConfig(AppConfig):
    name = 'User_Accounts'

    def ready(self):
        import User_Accounts.signals
