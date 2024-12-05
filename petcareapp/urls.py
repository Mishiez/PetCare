
from django.contrib import admin
from django.urls import path
from petcareapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('blogdetails/', views.blogdetails, name='blogdetails'),
    path('portfoliodetails/', views.portfoliodetails, name='portfoliodetails'),
    path('servicedetails/', views.servicedetails, name='servicedetails'),
    path('starter/', views.starter, name='starter'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('pricing/', views.pricing, name='pricing'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit, name='edit'),
    path('update/<int:id>', views.update, name='update'),



]
