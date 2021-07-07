from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView

from .models import Widget


class WidgetCreate(ListView):
    model = Widget
    fields = '__all__'

class WidgetDelete(ListView):
    model = Widget
    success_url = '/'



def home(request):
    return redirect ('widgets_index')

def widgets_index(request): 
    widgets = Widget.objects.all()
    return render(request, 'widgets/index.html', { 'widgets': widgets })

def widgets_detail(request, widget_id):
    widget = Widget.objects.get(id=widget_id)
    return render(request, 'widgets/index.html', { 'widgets': widgets })


class WidgetList(ListView):
    model = Widget