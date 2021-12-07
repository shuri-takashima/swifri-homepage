from django.urls import path
from . import views

app_name ='swifri'
urlpatterns =[
    path('', views.IndexView.as_view(), name='index'),
    path('art_list', views.Art_List_View.as_view(), name='art_list'),
    path('art_detail/<uuid:pk>', views.Art_Detail_View.as_view(), name='art_detail'),
]