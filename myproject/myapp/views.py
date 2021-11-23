from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test_view(request):
    print("request:" , request )
    return HttpResponse("""
    <HTML>
    <head></head>
    <body>
    hello world <br />
    this is our first
    </body>
    </HTML>
    """)