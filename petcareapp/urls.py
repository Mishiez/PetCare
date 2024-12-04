
from django.contrib import admin
from django.urls import path
from petcareapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blogdetails/', views.blogdetails, name='blogdetails'),
    path('portfoliodetails/', views.portfoliodetails, name='portfoliodetails'),
    path('servicedetails', views.service, name='servicedetails'),
    path('starter', views.starter, name='starter'),
]
