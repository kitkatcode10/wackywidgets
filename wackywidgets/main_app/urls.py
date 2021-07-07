from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('widgets/', views.widgets_index, name='widgets_index'), 
    path('widgets/<int:widget_id>/', views.widgets_detail, name='detail'),
    path('widgets/create/', views.WidgetCreate.as_view(), name='widgets_create'), 
    path('widgets/<int:pk>/delete/', views.WidgetDelete.as_view(), name='widgets_delete')
]