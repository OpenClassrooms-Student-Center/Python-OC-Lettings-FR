from datetime import datetime
from functools import wraps
from django.shortcuts import render
from sentry_sdk import capture_message, capture_exception
from django.urls import resolve


def capture_sentry_message(view_func):
    """
    A decorator to capture user visits and exceptions using Sentry.

    This decorator wraps a view function and captures a
    message when the view is visited by a user.
    If an exception occurs during the view's execution,
    the exception is captured and reported to Sentry.

    Args:
        view_func (function): The original view function to be wrapped.

    Returns:
        function: The wrapped view function with added Sentry message capturing.

    Example:
        @capture_sentry_message
        def my_view(request):
            # View logic
            ...
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        try:
            response = view_func(request, *args, **kwargs)
            resolved_url_name = resolve(request.path_info).url_name
            ip_user = request.META.get("REMOTE_ADDR")
            # message inside sentry
            capture_message(
                f"Page consultée {resolved_url_name} par l'utilisateur "
                f"{ip_user} le {datetime.today().strftime('%Y-%m-%d')} à "
                f"{datetime.now().strftime('%H:%M:%S')}",
                level="info",
            )

            return response
        except Exception as e:
            capture_exception(e)
            return render(request, "500.html", status=500)

    return wrapper
