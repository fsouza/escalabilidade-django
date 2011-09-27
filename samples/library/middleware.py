# -*- coding: utf-8 -*-

import cProfile
import sys

from cStringIO import StringIO
from django.conf import settings


class ProfileMiddleware(object):

    prof = None

    def process_request(self, request):
        if settings.DEBUG and 'prof' in request.GET:
            self.prof = cProfile.Profile()

    def process_view(self, request, callback, callback_args, callback_kwargs):
        if self.prof:
            return self.prof.runcall(callback, request, *callback_args, **callback_kwargs)

    def process_response(self, request, response):
        if self.prof:
            self.prof.disable()
            prof_out = StringIO()
            old_stdout = sys.stdout
            sys.stdout = prof_out

            self.prof.print_stats()

            sys.stdout = old_stdout
            stats = prof_out.getvalue()

            if response and response.content:
                response.content = '<pre>%s</pre>' % stats

        return response
