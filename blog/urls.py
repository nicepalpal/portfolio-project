from django.urls import path

from . import views

urlpatterns = [
    path('', views.allblogs, name='bloghome' ),
    #look for an int after the /blog and we will save as blog id
    path('<int:blog_id>/', views.detail, name='detail')
]
