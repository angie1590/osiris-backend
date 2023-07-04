"""
Django command to wait for the database to be available
"""
from __future__ import annotations

import time

from psycopg2 import OperationalError as Psycopg2Error

from django.core.management.base import BaseCommand
from django.db.utils import OperationalError
from django.db import connections

from typing import Any


class Command(BaseCommand):
    """Django command to wait for database."""
    help = "Django command to wait for database."

    def handle(self, *args: Any, **options: Any):
        pass
