# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.response import Response

from recipe_scrapers import scrape_me

# Create your views here.
@api_view()
def index(request):
  scraped = scrape_me('http://allrecipes.com/Recipe/Apple-Cake-Iv/Detail.aspx')

  title = scraped.title()
  # scrape_me.total_time()
  # scrape_me.ingredients()
  # scrape_me.instructions()

  return Response({"message": "Hello, world!", "recipe title": title})