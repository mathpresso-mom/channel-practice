import channels
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_channels.settings")
channel_layer = channels.asgi.get_channel_layer()