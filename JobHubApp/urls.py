from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('job_creations/', views.job_creation, name='job_creation'),
    path('job_listings/', views.job_listings, name='job_listings')
    # path('job_delete/', views.job_delete, name='job_delete')


]