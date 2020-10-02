from django.urls import path
from . import views

app_name="photos"

urlpatterns = [
    path("search/",views.search_results, name="search_results"),
    path("",views.homepage,name="homepage"),
    
]