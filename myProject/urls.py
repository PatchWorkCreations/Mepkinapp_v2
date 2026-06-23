from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.about, name='about'),
    path('virtual-tour/', views.virtual_tour, name='virtual-tour'),
    path('p/<slug:slug>/', views.page_detail, name='page-detail'),
    path('pray/', views.pray, name='pray'),
    path('psalter/', views.psalter, name='psalter'),
    path('calling', views.vocation, name='calling'),
    path('vocation/', views.vocation, name='vocation'),
]
