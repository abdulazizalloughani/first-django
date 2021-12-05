from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test_view(request):
    print("request:" , request )
    name = request.GET.get("username")
    c = {}
    c["z"] = name 
    c["age"] = 29
    c["major"] = "MIS"
    c["majors"] = ["MIS" , "accounting" , "finance" , "management"]
    return render(request , "test.html" ,c )