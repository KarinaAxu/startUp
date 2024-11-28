from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "store"
<<<<<<< HEAD

    def ready(self):
        import store.signals
=======
>>>>>>> eafb986a58cf6441ea3a5ec162772c32a4edb147
