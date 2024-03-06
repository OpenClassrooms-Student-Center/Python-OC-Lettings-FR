from sentry_sdk import set_tag, capture_exception, capture_message


def send_to_sentry_exception(tag1, tag2, exception):
    """ method to send report to Sentry when exception captured """

    set_tag(tag1, tag2)
    capture_exception(exception)


def send_to_sentry_message(tag1, tag2, message):
    """ method to send report to Sentry when exception captured """

    set_tag(tag1, tag2)
    capture_message(message)
