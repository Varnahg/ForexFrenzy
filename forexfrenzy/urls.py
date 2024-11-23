from django.urls import path, include
from . import views
from . import dash_apps

app_name = 'forexfrenzy'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.static_chart_view, name='FirstDashboard'),
]