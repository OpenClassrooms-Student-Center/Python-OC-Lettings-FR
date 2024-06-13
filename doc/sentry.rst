Sentry
========================================

Sentry is used in the views to check for errors with capture_exceptions
and tells us about the issue with capture_messages

It is configured inside our settings :
    .. code-block:: bash
        sentry_dsn = os.getenv('SENTRY_DSN')

Sentry_DSN is your secret variable in .env file !
