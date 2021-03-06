from __future__ import absolute_import

from ircb.models import create_tables

from .network import NetworkStore
from .client import ClientStore
from .channel import ChannelStore
from .user import UserStore


def initialize():
    create_tables()
    NetworkStore.initialize()
    ClientStore.initialize()
    ChannelStore.initialize()
    UserStore.initialize()

__all__ = [
    'ClientStore',
    'NetworkStore',
    'ChannelStore',
    'UserStore'
]
