from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def widget_index(request):
    return render(request, 'index.html')

def widget_index(request): 
    widgets = Widget.objects.filter(user=request.user)
    return render(request, 'widgets/index.html', { 'widgets': widgets })