from django.urls import path
from api import views


urlpatterns = [
    path('', views.home,name="home"),
    path('view-eosl', views.view_eosl,name="view-eosl"),
]
