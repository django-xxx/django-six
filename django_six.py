# -*- coding: utf-8 -*-

# https://github.com/django/django/blob/fc94944183f1f1325824ee0ef1f49d737ec86d4a/django/db/__init__.py#L101-L112
# close_connection is superseded by close_old_connections
# RemovedInDjango18Warning
try:
    from django.db import close_old_connections as close_connection
except ImportError:
    from django.db import close_connection

close_old_connections = close_connection
