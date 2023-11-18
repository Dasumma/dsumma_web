from django.shortcuts import render

# Create your views here.

def newView(request):
    return render(request, 'BaseSite.html', context=None)