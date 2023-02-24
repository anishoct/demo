# from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Team
# Create your views here.
# def demo(request):
#     return HttpResponse("hello world")


def about(request):
    obj=Place.objects.all()
    obj1 = Team.objects.all()
    return render(request, "index.html",{'value':obj,'result':obj1})


# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     add = x+y
#     mul=x*y
#     sub=x-y
#     div=x/y
#     return render(request, "results.html", {'w':add,'a':mul,'b':sub,'c':div})
#

# def contact(request):
#     return HttpResponse("hallo anish")
# def details(request):
#     return HttpResponse("i love my india")
#
# def thanks(request):
#     return render(request,"thanks.html")

