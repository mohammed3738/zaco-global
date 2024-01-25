from django.urls import path
from api import views


urlpatterns = [
    path('', views.home,name="home"),
    path('view-eosl', views.view_eosl,name="view-eosl"),
    path('detail-view-eosl/<str:name>', views.detail_view_eosl,name="detail-view-eosl"),
]
