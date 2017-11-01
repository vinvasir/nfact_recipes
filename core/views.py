# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from recipe_scrapers import scrape_me

# Create your views here.
@api_view()
def index(request):
  scraped = scrape_me('http://allrecipes.com/Recipe/Apple-Cake-Iv/Detail.aspx')

  title = scraped.title()
  time = scraped.total_time()
  ingredients = scraped.ingredients()
  instructions = scraped.instructions()

  return Response({"message": "Hello, world!", "recipe title": title})

@api_view()
@permission_classes((IsAuthenticated,))
def allrecipes(request, slug):
  endpoint = 'http://allrecipes.com/Recipe/' + slug + '/Detail.aspx'

  scraped = scrape_me(endpoint)

  title = scraped.title()
  time = scraped.total_time()
  ingredients = scraped.ingredients()
  instructions = scraped.instructions()

  return Response(
    {"Recipe": {
      "title": title, 
      "time": time, 
      "ingredients": ingredients, 
      "instructions": instructions
      }, 'auth': request.auth,
    })