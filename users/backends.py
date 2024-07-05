from django.conf import settings
from djangosaml2.backends import Saml2Backend


class CustomSaml2Backend(Saml2Backend):
    def save_user(self, user: settings.AUTH_USER_MODEL, *args, **kwargs):
        return super().save_user(user, *args, **kwargs)
    def _update_user(self, user, attributes: dict, attribute_mapping: dict, force_save: bool = False):
        return super()._update_user(user, attributes, attribute_mapping, force_save)