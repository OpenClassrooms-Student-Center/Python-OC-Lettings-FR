"""
Module for monitoring with Sentry
"""
import logging
import sentry_sdk

from sentry_sdk.integrations.logging import LoggingIntegration

from config import SENTRY_KEY

logger = logging.getLogger(__name__)


def init_sentry():
    """
    Method to initialize sentry integration
    """
    logging.basicConfig(level=logging.INFO)

    sentry_logging = LoggingIntegration(
        level=logging.INFO,
        event_level=logging.ERROR,
    )

    sentry_sdk.init(
        dsn=SENTRY_KEY,
        # Add request headers and IP for users,
        # see https://docs.sentry.io/platforms/python/data-management/data-collected/ for more info
        send_default_pii=True,

        # Enable logs to be sent to Sentry
        enable_logs=True,

        integrations=[sentry_logging]
    )
