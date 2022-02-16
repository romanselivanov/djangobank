from django.apps import AppConfig


class NezbankConfig(AppConfig):
    name = 'nezbank'
    verbose_name = 'Пользователи и аккаунты'

    def ready(self):
        import nezbank.signals
