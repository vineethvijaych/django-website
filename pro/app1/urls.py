from django.urls import path
from.import views

urlpatterns =[
    path('',views.home,name="home"),
    path('add2',views.add2,name="add2"),
    path('view',views.view,name="add")
]