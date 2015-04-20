from django.db import models
from registration.signals import user_registered
from xmpp_handler import xmpp_handler
# Create your models here.


def user_registered_callback(sender, user, request, **kwargs):
    xmpp = user.username
    xmpp_handler.add_controller(name=xmpp, password=xmpp)
    xmpp_handler.friends_with_admin(user=xmpp)



user_registered.connect(user_registered_callback)