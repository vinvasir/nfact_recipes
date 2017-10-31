# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view()
def index(request):
  return Response({"message": "Hello, world!"})