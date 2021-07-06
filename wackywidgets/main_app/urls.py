from django.urls import path
from . import views

urlpatterns = [
    path('widgets/', views.widget_index, name='index'), 
    # path('widgets/<int:widget_id>/', views.widgets_detail, name='detail'),
    # path('widgets/create/', views.WidgetCreate.as_view(), name='widgets_create'), 
]