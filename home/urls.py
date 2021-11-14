from django.contrib import admin
from django.urls import path, include
from home import views

#Django admin header customization
admin.site.site_header = "Login to Developer Tabinda"
admin.site.site_title = "Welcome to Tabinda's Dashboard"
admin.site.index_title = "Welcome to this portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.project, name='project'),
    path('experience/', views.experience, name='experience'),
    path('contact', views.contact, name='contact'),
    path('success', views.success, name='contact'),
]
