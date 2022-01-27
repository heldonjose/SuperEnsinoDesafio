# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.utils.functional import SimpleLazyObject

from django.core.exceptions import ValidationError
from django.contrib import messages

# class _HandleHttpResponseRedirect(HttpResponseRedirect):
#     def __init__(self, request, *args, **kwargs):
#         redirect_to = request.META.get('HTTP_REFERER', '/')
#         super(_HandleHttpResponseRedirect, self).__init__(
#             redirect_to, *args, **kwargs)
#
#
# class HierarchyMiddleware(MiddlewareMixin):
#     def process_exception(self, request, exception):
#         response = None
#         if isinstance(exception, ValidationError):
#             if request.path.startswith(('/admin/')):
#                 message = exception.message
#                 messages.error(request, message)
#                 return _HandleHttpResponseRedirect(request)
#         return response