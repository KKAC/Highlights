from django.http import HttpResponse

from fb_bot.messenger_manager import send_error_message
from fb_highlights.views import HighlightsBotView

from raven.contrib.django.raven_compat.models import client, got_request_exception


class MessengerMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def process_exception(self, request, exception):
        id = HighlightsBotView.LATEST_SENDER_ID
        send_error_message(id)

        # Make sure the exception signal is fired for Sentry
        client.user_context({
            'user_id': id
        })
        got_request_exception.send(sender=self, request=request)

        return HttpResponse()
