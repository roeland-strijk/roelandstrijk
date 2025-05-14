from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns=[
    path('', views.radio_log, name="form133"),
    #path('logs', views.radio_lognext, name="form133next"),
    path('logs', views.radio_log_combined, name="form133next"),
    path('logs/', views.radio_log_combined, name='logs')
    
    
]
           