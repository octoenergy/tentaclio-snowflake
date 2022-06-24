"""This package implements the tentaclio snowflake client """
from tentaclio import *  # noqa

from .clients.snowflake_client import ClientClassName


# Add DB registry
DB_REGISTRY.register("snowflake", ClientClassName)  # type: ignore
